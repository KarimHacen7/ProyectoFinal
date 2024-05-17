import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backend_bases import MouseEvent

class BlittedCursor:
    """
    A cross-hair cursor using blitting for faster redraw.
    """
    def __init__(self, ax):
        self.ax = ax
        self.background = None
        self.vertical_line = ax.axvline(color='k', lw=0.8, ls='--', animated=True)
        # text location in axes coordinates
        self._creating_background = False
        ax.figure.canvas.mpl_connect('draw_event', self.on_draw)

    def on_draw(self, event):
        self.create_new_background()

    def create_new_background(self):
        if self._creating_background:
            # discard calls triggered from within this function
            return
        self._creating_background = True
        self.ax.figure.canvas.draw()
        self.background = self.ax.figure.canvas.copy_from_bbox(self.ax.bbox)
        self._creating_background = False

    def on_mouse_move(self, event):
        if self.background is None:
            self.create_new_background()
        if not event.inaxes:
                self.ax.figure.canvas.restore_region(self.background)
                self.ax.figure.canvas.blit(self.ax.bbox)
        else:
            # update the line positions
            x = event.xdata
            self.vertical_line.set_xdata([x])

            self.ax.figure.canvas.restore_region(self.background)

            self.ax.draw_artist(self.vertical_line)

            self.ax.figure.canvas.blit(self.ax.bbox)


x = np.arange(0, 1, 0.01)
y = np.sin(2 * 2 * np.pi * x)

fig, ax = plt.subplots()
ax.set_title('Blitted cursor')
ax.plot(x, y, 'o')
blitted_cursor = BlittedCursor(ax)
fig.canvas.mpl_connect('motion_notify_event', blitted_cursor.on_mouse_move)

plt.show()


# Basicamente hay que 
#   Definir todas las weas de siempre
#   defini lo que vayas a dibujar blitteado con el argumento animated=True
#   Dibuja lo que queda constante y guardalo con figure.canvas.copy_from_bbox DESPU[ES DEL DRAW()]
#   Hacete un cerrojo para ignorar los callback de eventos mientras dibujas
#   luego, libera el cerrojo y llama a draw_artist(lo que vayas a blittear)
#   finalmente, llam[a a figure.canvas.blit(self.ax.bbox)
