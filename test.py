import { test, expect } from "@playwright/test";

test.describe("Camera Vision Page", () => {

  test("Start camera button initializes webcam UI", async ({ page }) => {
    await page.goto("http://localhost:5500/camera-vision.html");

    await page.click("#startCameraBtn");

    await expect(page.locator("#videoContainer")).toBeVisible();
    await expect(page.locator("#stopCameraBtn")).toBeVisible();
    await expect(page.locator("#cameraControls")).toBeHidden();
  });

  test("Stop camera button resets UI", async ({ page }) => {
    await page.goto("http://localhost:5500/camera-vision.html");

    await page.click("#startCameraBtn");
    await page.click("#stopCameraBtn");

    await expect(page.locator("#startCameraBtn")).toBeVisible();
    await expect(page.locator("#detectionText")).toContainText("Camera stopped");
  });

});




import { test, expect } from "@playwright/test";
import path from "path";

test("Image upload sends data and displays results", async ({ page }) => {
  await page.goto("http://localhost:5500/camera-vision.html");

  const filePath = path.resolve("tests/assets/test-image.jpg");

  await page.setInputFiles("#fileInput", filePath);

  await expect(page.locator("#uploadedFilesList")).toBeVisible();
  await expect(page.locator("#filesGrid img")).toBeVisible();
  await expect(page.locator(".detection-badge")).toHaveCountGreaterThan(0);
});

