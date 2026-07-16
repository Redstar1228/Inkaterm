# Changelog

## [2.0.0] - 2026-07-16

This release is a complete redesign of Inkaterm, introducing a new API, editable images, and a much more flexible rendering system.

### Added
- New `Ink` API for reusable renderer configuration.
- Images are now represented as editable `Image` objects instead of being rendered immediately.
- Support for loading images from:
  - `str`
  - `bytes`
  - `bytearray`
  - `memoryview`
  - `BytesIO`
- Image resizing with `Image.resize()`.
- Built-in image filters with method chaining.
- `fill_background` rendering mode.
- Automatic True Color detection.
- LZ4-compressed disk cache.
- Runtime argument type validation.
- Detailed exception messages.
- `__repr__()` implementations for `Ink` and `Image`.

### Changed
- Completely redesigned public API.
- `Ink.image()` now returns an editable `Image` object.
- Rendering settings can now be overridden for each image individually.
- Improved rendering performance.
- Improved cache implementation.
- Updated documentation and API reference.

### Fixed
- Fixed multiple rendering issues.
- Fixed invalid color detection.
- Better handling of invalid arguments.
- Various internal bug fixes and code cleanup.