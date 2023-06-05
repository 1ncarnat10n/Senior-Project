import pygame
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        self.frames = {
			'flame': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/flame/frames'),
			'aura': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/aura'),
			'heal': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/heal/frames'),
			
			'claw': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/claw'),
			'slash': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/slash'),
			'sparkle': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/sparkle'),
			'leaf_attack': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf_attack'),
			'thunder': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/thunder'),

			'squid': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/smoke_orange'),
			'raccoon': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/raccoon'),
			'spirit': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/nova'),
			'bamboo': import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/bamboo'),
			
			'leaf': (
				import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf1'),
				import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf2'),
				import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf3'),
				import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf4'),
				import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf5'),
				import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf6'),
				self.reflect_images(import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf1')),
				self.reflect_images(import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf2')),
				self.reflect_images(import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf3')),
				self.reflect_images(import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf4')),
				self.reflect_images(import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf5')),
				self.reflect_images(import_folder('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/particles/leaf6'))
				)
			}

    def reflect_images(self, frames):
        new_frames = []

        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self, pos, groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]
    
    def update(self):
        self.animate()