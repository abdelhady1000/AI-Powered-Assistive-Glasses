/**
 * @jest-environment jsdom
 */

const fs = require("fs");
const path = require("path");

describe("Frontend Pages Load Correctly", () => {

  test("Camera Vision page has Start Camera button", () => {
    const html = fs.readFileSync(
      path.resolve(__dirname, "../camera-vision.html"),
      "utf8"
    );
    document.documentElement.innerHTML = html;
    const btn = document.getElementById("startCameraBtn");
    expect(btn).not.toBeNull();
  });

  test("Products page shows Products section", () => {
    const html = fs.readFileSync(
      path.resolve(__dirname, "../products.html"),
      "utf8"
    );
    document.documentElement.innerHTML = html;
    expect(document.body.textContent).toContain("Our Products");
  });

  test("Contact page has form", () => {
    const html = fs.readFileSync(
      path.resolve(__dirname, "../contact.html"),
      "utf8"
    );
    document.documentElement.innerHTML = html;
    const form = document.querySelector("form");
    expect(form).not.toBeNull();
  });

});
