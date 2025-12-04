# SnapGrid - Modern Photo Arranger

<div align="center">

![SnapGrid Banner](https://img.shields.io/badge/SnapGrid-Photo%20Arranger-blue?style=for-the-badge)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge)]()

**Drag, Drop & Arrange Your Photos with Ease**

A powerful, modern web-based photo arrangement tool that helps you create beautiful PDF layouts from your photo collections.

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [Usage](#usage) • [Contributing](#contributing)

</div>

---

## 📸 Features

### Core Functionality
- **🖱️ Drag & Drop Interface** - Intuitive photo placement with visual feedback
- **📄 Multi-Page Layouts** - Automatically create multiple pages based on photo count
- **🎨 Professional Image Editor** - Built-in editor with crop, rotate, and comprehensive adjustments
- **📊 Multiple Grid Layouts** - Flexible row/column configurations (up to 10x10)
- **🔄 Orientation Support** - Switch between landscape and portrait modes
- **📐 Aspect Ratio Control** - 8 preset ratios plus free-form option
- **💾 PDF Generation** - High-quality PDF output with embedded images
- **👁️ Live Preview** - Real-time PDF preview before generation

### Image Editing Capabilities
- **Crop & Transform**
  - Interactive crop with 8 resize handles
  - Aspect ratio locking (16:9, 4:3, 3:2, 1:1, etc.)
  - Rotation (90°, 180°, 270°, or custom)
  - Zoom (50% - 200%)
  - Flip horizontal/vertical

- **Light Adjustments**
  - Brightness
  - Contrast
  - Exposure
  - Shadows
  - Whites & Blacks

- **Color Adjustments**
  - Temperature
  - Tint
  - Vibrance
  - Saturation
  - Hue shift

- **Effects**
  - Texture
  - Clarity
  - Dehaze
  - Vignette
  - Grain
  - Sharpen

### Advanced Features
- **🎯 Image Fit Modes** - Cover, Contain, Fill, Scale-down, Original
- **📏 Paper Size Presets** - A0-A6, 4×6, 5×7, 8×10, 8×12, 12×18
- **💾 Settings Persistence** - All preferences saved to localStorage
- **🔍 High-Resolution Crop** - Maintains original image quality
- **📊 Image Info Display** - Shows resolution and aspect ratio
- **🏷️ PDF Watermarking** - Customizable watermark on each page
- **📝 PDF Metadata** - Comprehensive metadata embedding

## 🎯 Use Cases

- 📚 Creating photo albums and portfolios
- 🎓 School project presentations
- 📅 Event photo compilations
- 🏢 Business photo catalogs
- 👨‍👩‍👧‍👦 Family photo arrangements
- 🎨 Art and design portfolios
- 📰 Newsletter layouts
- 🏠 Real estate listings

## 🚀 Quick Start

### Prerequisites
- Modern web browser (Chrome, Firefox, Edge, Safari)
- No installation required!

### Running the Application

1. **Clone the repository**
   ```bash
   git clone https://github.com/TusharNeje/photo-arranger.git
   cd photo-arranger
   ```

2. **Open in browser**
   - Simply open `index.html` in your web browser
   - Or use a local server:
     ```bash
     # Python 3
     python -m http.server 8000
     
     # Node.js
     npx serve
     ```

3. **Start arranging!**
   - Upload photos
   - Drag them to the canvas
   - Customize layout
   - Generate PDF

## 📖 Usage Guide

### Basic Workflow

1. **Upload Photos**
   - Click the upload area or drag & drop images
   - Supports multiple image formats (JPG, PNG, etc.)

2. **Configure Layout**
   - Choose orientation (Landscape/Portrait)
   - Select paper size (A4, A3, etc.)
   - Set grid dimensions (rows × columns)
   - Adjust margins and spacing

3. **Arrange Photos**
   - Drag photos from the library to canvas grid
   - Use pagination to navigate multiple pages
   - Remove photos with the × button
   - Use "Auto Fill" for quick arrangement

4. **Edit Images** (Optional)
   - Double-click any placed photo
   - Apply crop, rotate, and filters
   - Maintain original resolution
   - Save changes

5. **Generate PDF**
   - Click "Preview PDF" to see the final layout
   - Review in the embedded PDF viewer
   - Click "Generate PDF" to download

### Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Next Page | Arrow Right |
| Previous Page | Arrow Left |
| Close Editor | Escape |
| Save Editor | Ctrl/Cmd + Enter |

## 🎨 Customization

### Layout Settings
- **Paper Size**: A0 to A6, custom dimensions
- **Grid**: 1×1 up to 10×10
- **Margins**: Adjustable page and grid spacing
- **Orientation**: Landscape or Portrait
- **Box Ratio**: 16:9, 4:3, 3:2, 1:1, and more

### Image Fit Modes
- **Cover**: Fill entire box (crop if needed)
- **Contain**: Fit entire image with padding
- **Fill**: Stretch to fill
- **Scale-down**: Fit without enlarging
- **Original**: Use original size

## 💾 Settings Persistence

All your preferences are automatically saved:
- Orientation selection
- Image fit mode
- Box aspect ratio
- Paper size
- Grid dimensions
- Margin settings

Settings persist across browser sessions using localStorage.

## 🔧 Technical Details

### Technologies Used
- **HTML5** - Structure and Canvas API
- **CSS3** - Modern styling with custom properties
- **JavaScript** - ES6+ features
- **PDF-lib.js** - PDF generation and manipulation
- **Bootstrap 5.3** - UI framework
- **Bootstrap Icons** - Icon library

### Browser Support
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Image Processing
- Client-side processing (no server required)
- Maintains full resolution during editing
- Efficient canvas-based rendering
- High-quality JPEG output (95% quality)

## 📂 Project Structure

```
photo-arranger/
│
├── index.html          # Main application file
├── README.md           # This file
├── input/              # Default input folder
├── output/             # Default output folder
├── application.py      # Python utilities (optional)
└── main.py            # Python utilities (optional)
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Guidelines
- Follow existing code style
- Test across multiple browsers
- Update documentation as needed
- Keep commits atomic and well-described

## 🐛 Known Issues

- Very large images (>10MB) may cause performance issues
- PDF generation with 100+ images may take time
- Some older browsers may not support all features

## 🗺️ Roadmap

- [ ] Add templates for common layouts
- [ ] Support for text overlays
- [ ] Batch processing capabilities
- [ ] Cloud storage integration
- [ ] Mobile app version
- [ ] Print optimization
- [ ] Multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**TusharNeje** ([@TusharNeje](https://github.com/TusharNeje))

## 🙏 Acknowledgments

- PDF-lib for PDF generation capabilities
- Bootstrap team for the excellent UI framework
- All contributors and users of SnapGrid

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/TusharNeje/photo-arranger/issues)
- **Discussions**: [GitHub Discussions](https://github.com/TusharNeje/photo-arranger/discussions)
- **Email**: your.email@example.com

## ⭐ Show Your Support

If you find this project helpful, please consider giving it a star on GitHub!

---

<div align="center">

**Made with ❤️ by [@TusharNeje](https://github.com/TusharNeje)**

*Document Generated Programmatically via SnapGrid*

</div>
