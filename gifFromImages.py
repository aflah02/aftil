from PIL import Image
import os

def make_gif(save_name):
    frames = []
    imgs = [filename for filename in os.listdir('plots')]

    for i in imgs:
        new_frame = Image.open(f"plots/{i}")
        frames.append(new_frame)
    
    # Save into a GIF file that loops forever
    frames[0].save(f'gifs/{save_name}.gif', format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=300, loop=0)

