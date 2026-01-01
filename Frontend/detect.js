const API_URL = "http://127.0.0.1:8000"; // backend URL

// ===== CAMERA ELEMENTS =====
const startBtn = document.getElementById('startCameraBtn');
const stopBtn = document.getElementById('stopCameraBtn');
const cameraFeed = document.getElementById('cameraFeed');
const videoContainer = document.getElementById('videoContainer');
const detectionText = document.getElementById('detectionText');
const detectionBadges = document.getElementById('detectionBadges');
const cameraControls = document.getElementById('cameraControls');
const cameraMessage = document.getElementById('cameraMessage');

let stream;
let detectionInterval;

// ===== START CAMERA =====
startBtn.addEventListener('click', async () => {
    try {
        videoContainer.style.display = 'block';
        startBtn.style.display = 'none';
        stopBtn.style.display = 'inline-block';
        cameraControls.style.display = 'none';

        stream = await navigator.mediaDevices.getUserMedia({ video: true });
        cameraFeed.srcObject = stream;
        cameraFeed.play();

        detectionInterval = setInterval(detectCameraFrame, 2000); // every 2 seconds
    } catch(err) {
        console.error("Camera error:", err);
        alert("Could not start camera. Please allow camera access.");
    }
});

// ===== STOP CAMERA =====
stopBtn.addEventListener('click', () => {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        clearInterval(detectionInterval);
        detectionText.textContent = 'Camera stopped';
        detectionBadges.style.display = 'none';
        stopBtn.style.display = 'none';
        startBtn.style.display = 'inline-block';
        cameraControls.style.display = 'flex';
    }
});

// ===== DETECT FRAME FROM CAMERA =====
async function detectCameraFrame() {
    if (!cameraFeed.videoWidth) return; // skip if video not ready

    const canvas = document.createElement('canvas');
    canvas.width = cameraFeed.videoWidth;
    canvas.height = cameraFeed.videoHeight;
    canvas.getContext('2d').drawImage(cameraFeed, 0, 0);

    const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/jpeg'));
    const formData = new FormData();
    formData.append('file', blob, 'frame.jpg');

    try {
        const res = await fetch(`${API_URL}/detect-image/`, {
            method: 'POST',
            body: formData
        });
        const data = await res.json();

        // Update detection text
        detectionText.textContent = data.sentence;

        // Update badges
        detectionBadges.innerHTML = '';
        data.objects.forEach(obj => {
            const badge = document.createElement('span');
            badge.className = 'detection-badge';
            badge.textContent = obj;
            detectionBadges.appendChild(badge);
        });
        detectionBadges.style.display = data.objects.length ? 'block' : 'none';

        // Play audio
        const audio = new Audio(`${API_URL}${data.audio_url}`);
        audio.play();

    } catch(err) {
        console.error("Detection error:", err);
    }
}

// ===== FILE UPLOAD ELEMENTS =====
const chooseFilesBtn = document.getElementById('chooseFilesBtn');
const fileInput = document.getElementById('fileInput');
const uploadedFilesList = document.getElementById('uploadedFilesList');
const filesGrid = document.getElementById('filesGrid');
const fileCount = document.getElementById('fileCount');

chooseFilesBtn.addEventListener('click', () => fileInput.click());

fileInput.addEventListener('change', async () => {
    const files = Array.from(fileInput.files);
    if (!files.length) return;

    uploadedFilesList.style.display = 'block';
    filesGrid.innerHTML = '';
    fileCount.textContent = `(${files.length})`;

    for (const file of files) {
        const fileType = file.type.startsWith('video') ? 'video' : 'image';
        const fileUrl = URL.createObjectURL(file);

        // Show preview
        const wrapper = document.createElement('div');
        wrapper.className = 'border border-[#302839] rounded-lg p-2 bg-[#141118]';
        wrapper.innerHTML = fileType === 'image' ?
            `<img src="${fileUrl}" class="rounded-lg w-full object-contain"/>` :
            `<video src="${fileUrl}" controls class="rounded-lg w-full object-contain"></video>`;
        filesGrid.appendChild(wrapper);

        // Send to backend
        const formData = new FormData();
        formData.append('file', file, file.name);

        try {
            const endpoint = fileType === 'video' ? '/detect-video/' : '/detect-image/';
            const res = await fetch(`${API_URL}${endpoint}`, {
                method: 'POST',
                body: formData
            });
            const data = await res.json();

            // Show results under file preview
            const resultsDiv = document.createElement('div');
            resultsDiv.className = 'mt-2';
            resultsDiv.innerHTML = `
                <p class="text-[#ff3b84] font-semibold">${data.sentence}</p>
                <div class="flex flex-wrap gap-2 mt-1"></div>
            `;
            data.objects.forEach(obj => {
                const badge = document.createElement('span');
                badge.className = 'detection-badge';
                badge.textContent = obj;
                resultsDiv.querySelector('div').appendChild(badge);
            });
            wrapper.appendChild(resultsDiv);

            // Play audio
            const audio = new Audio(`${API_URL}${data.audio_url}`);
            audio.play();

        } catch(err) {
            console.error("File detection error:", err);
        }
    }
});
