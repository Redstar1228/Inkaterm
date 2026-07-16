# Inkaterm 🔏

Convert images into beautiful colored ASCII art directly in your terminal with a fast, customizable, and lightweight Python library.

![Downloads](https://static.pepy.tech/personalized-badge/inkaterm?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads&cachebuster=1)
[![GitHub stars](https://img.shields.io/github/stars/Redstar1228/Inkaterm?style=social)](https://github.com/Redstar1228/Inkaterm)
![GitHub code size](https://img.shields.io/github/languages/code-size/Redstar1228/Inkaterm)
![GitHub issues](https://img.shields.io/github/issues/Redstar1228/Inkaterm)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Redstar1228/Inkaterm)
![GitHub last commit](https://img.shields.io/github/last-commit/Redstar1228/Inkaterm)
![Python](https://img.shields.io/pypi/pyversions/inkaterm)
![License](https://img.shields.io/github/license/Redstar1228/Inkaterm)

---

## ✨ Features

- 🚀 Fast rendering
- 🎨 ANSI TrueColor and 256-color support
- 🖼️ Convert images into colored ASCII art
- 💾 Smart disk cache with LZ4 compression
- ⚡ Optimized rendering pipeline
- 🔧 Highly customizable output
- 📂 Supports file paths, bytes, bytearray, memoryview and BytesIO
- 🎭 Built-in image filters
- 🐍 Pure Python implementation
- 🔗 Method chaining support

---

# 📦 Installation

```bash
pip install inkaterm
```

---

# 🚀 Quick Start

```python
import inkaterm

ink = inkaterm.Ink()

image = ink.image("image.png")
image.resize(75, 75)

print(image)
```

---

# 🖼️ Output

### ANSI TrueColor

<p align="center">
    <img src="images/true_color.jpg" width="600" alt="TrueColor Preview">
</p>

### ANSI 256 Colors

<p align="center">
    <img src="images/256_color.jpg" width="600" alt="256 Color Preview">
</p>

> All screenshots were captured inside the Termux terminal.

---

# ⚡ Performance

Inkaterm includes an optimized cache system.

Example:

```text
Image size: 1000 × 1000

First render:
≈ 9 s

From cache:
≈ 200 ms
```

Cache files are compressed using **LZ4**.

Example:

```text
Original cache:
12 MB

Compressed:
218 KB
```

---

# ⚙️ Basic Usage

## Create an Ink instance

```python
import inkaterm

ink = inkaterm.Ink()
```

---

## Load an image

```python
image = ink.image("cat.png")
```

---

## Resize

```python
image.resize(120, 80)
```

---

## Apply filters

```python
image.filter \
    .grayscale() \
    .contrast(1.5) \
    .brightness(15)

print(image)
```

---

## Method chaining

```python
image.resize(80, 80)

image.filter \
    .dreamy() \
    .contrast(1.4) \
    .sharpness(2)

print(image)
```

---

# 📚 API Reference

## `inkaterm.Ink`

Main rendering class.

### Constructor

```python
Ink(
    root_dir=".",
    char="██",
    fill_background=False,
    cache=False,
    cache_dir="inkaterm_cache",
    true_color=None
)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `root_dir` | `str` | `"."` | Base directory for relative image paths. |
| `char` | `str` | `"██"` | Character(s) used for rendering. |
| `fill_background` | `bool` | `False` | Uses ANSI background colors instead of foreground text colors. |
| `cache` | `bool` | `False` | Enables disk cache. |
| `cache_dir` | `str` | `"inkaterm_cache"` | Cache directory. |
| `true_color` | `bool \| None` | `None` | Enables or disables TrueColor. When `None`, Inkaterm detects terminal support automatically. |

---

## `Ink.image()`

Loads an image.

```python
image = ink.image(
    file,
    char=None,
    fill_background=None,
    cache=None,
    cache_dir=None,
    true_color=None
)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `file` | `str`, `bytes`, `bytearray`, `memoryview`, `BytesIO` | Image source. |
| `char` | `str \| None` | Overrides the default rendering character. |
| `fill_background` | `bool \| None` | Overrides the renderer background mode. |
| `cache` | `bool \| None` | Enables or disables cache for this image only. |
| `cache_dir` | `str \| None` | Overrides the cache directory. |
| `true_color` | `bool \| None` | Overrides color mode for this image. |

Returns:

```python
Image
```

---

# 🖼️ Image

Represents a loaded image.

---

## `resize()`

```python
image.resize(width, height)
```

| Parameter | Type |
|-----------|------|
| `width` | `int` |
| `height` | `int` |

Returns:

```python
Image
```

---

## Rendering

```python
print(image)
```

or

```python
str(image)
```

---

# 🎨 Filters

Access filters through

```python
image.filter
```

---

## `apply()`

```python
image.filter.apply(red, green, blue)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `red` | `float` | Red channel multiplier. |
| `green` | `float` | Green channel multiplier. |
| `blue` | `float` | Blue channel multiplier. |

---

## Available Filters

| Method | Description |
|---------|-------------|
| `brightness(value)` | Adjust image brightness. |
| `contrast(factor)` | Adjust image contrast. |
| `invert()` | Invert image colors. |
| `grayscale()` | Convert the image to grayscale. |
| `sharpness(amount)` | Increase image sharpness. |
| `blur(radius)` | Apply a box blur. |
| `gaussian_blur(radius)` | Apply Gaussian blur. |
| `sepia()` | Apply a sepia effect. |
| `vintage()` | Apply a vintage effect. |
| `cool_blue()` | Apply a cool blue effect. |
| `retro_red()` | Apply a retro red effect. |
| `neon_green()` | Apply a neon green effect. |
| `dreamy()` | Apply a dreamy color effect. |
| `dark_mood()` | Apply a dark mood effect. |

Every filter returns the current `Filter` object, allowing method chaining.

Example:

```python
image.filter \
    .grayscale() \
    .contrast(1.5) \
    .brightness(20)
```

---

# 📂 Supported Image Sources

| Source | Supported |
|---------|:---------:|
| File path (`str`) | ✅ |
| `bytes` | ✅ |
| `bytearray` | ✅ |
| `memoryview` | ✅ |
| `BytesIO` | ✅ |

---

# ⚠️ Exceptions

| Exception | Description |
|-----------|-------------|
| `ImageNotFoundError` | Image file does not exist. |
| `InvalidTypeError` | Invalid argument type. |
| `InvalidSizeError` | Width or height is less than 1. |
| `FilterError` | Invalid filter parameter. |

---

# 📝 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you like Inkaterm, consider giving the repository a ⭐ on GitHub.