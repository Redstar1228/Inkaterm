from .renderer import Renderer

class Render:
    def __str__(self):
        if getattr(self, "filter", None) is not None:
            self.img = self.filter.img
        return Renderer(self._char, self._fill_background, self._cache, self._cache_dir, self._true_color).render_image(self.img)