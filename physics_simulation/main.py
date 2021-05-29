
import pymunk
import arcade
from math import degrees


space = pymunk.Space()
space.gravity = 0, -1000

mass = 1
radius = 15
el = 1


class PhysicsSprite(arcade.Sprite):
    def __init__(self, pymunk_shape, filename):
        super().__init__(filename, center_x=pymunk_shape.body.position.x, center_y=pymunk_shape.body.position.y)
        self.pymunk_shape = pymunk_shape


class BoxSprite(PhysicsSprite):
    def __init__(self, pymunk_shape, filename, width, height):
        super().__init__(pymunk_shape, filename)
        self.width = width
        self.height = height


segment_shape1 = pymunk.Segment(space.static_body, (0,700), (1480,700), 2)
segment_shape1.elasticity = el
segment_shape1.friction = 2
a = input()
seg = []
space.add(segment_shape1)
seg.append(segment_shape1)

segment_shape2 = pymunk.Segment(space.static_body, (0,30), (1480,30), 2)
segment_shape2.elasticity = el
segment_shape2.friction = 2
space.add(segment_shape2)
seg.append(segment_shape2)

segment_shape3 = pymunk.Segment(space.static_body, (1450,0), (1450,720), 2)
segment_shape3.elasticity = el
segment_shape3.friction = 2
space.add(segment_shape3)
seg.append(segment_shape3)

segment_shape4 = pymunk.Segment(space.static_body, (30, 0), (30,720), 2)
segment_shape4.elasticity = el
segment_shape4.friction = 2
space.add(segment_shape4)
seg.append(segment_shape4)


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(10, 10)

        arcade.set_background_color(arcade.color.BLACK)

        self.sprites = arcade.SpriteList()
        self.shape_being_dragged = None
        self.mouse_pos = (0, 0, 0, 0)
        self.mode = 0
        self.mode_filter = {0: 'coinGold.png', 1: 'pointer.png', 2: 'boxCrate_double.png', 3: 'pinjoint.png', 4: 'spring.png', 5: 'electric-motor.png', 6: 'line.png'}
        #self.mode_filter = {0: 'resources/images/items/coinGold.png', 1: 'pointer.png',
                            #2: 'create', 3: 'create pin_joint'}
        self.joints = []
        self.shape_1 = None
        self.shape_2 = None
        self.gravity = 0
        self.gravity_filter = {0: 'flatDark26.png', 1: 'flatDark11.png', 2: 'flatDark25.png', 3: 'flatDark23.png', 4: 'flatDark24.png', 5: 'layout.png'}
        self.gravity_sprite = arcade.Sprite(self.gravity_filter[self.gravity], scale=.5, center_x=150, center_y=650)
        self.mode_sprite = arcade.Sprite(self.mode_filter.get(self.mode, self.mode), scale=.3, center_x=160, center_y=680)


    def on_draw(self):
        arcade.start_render()
        for i in seg:
            #print(i.a, i.b)
            arcade.draw_lines([i.a, i.b], arcade.color.BRIGHT_MAROON, 4)
        #print('d')
        for joint in self.joints:
            if isinstance(joint, pymunk.DampedSpring):
                arcade.draw_line(joint.a.position.x, joint.a.position.y, joint.b.position.x, joint.b.position.y,
                                 arcade.color.GRAPE, 3)
            else: arcade.draw_line(joint.a.position.x, joint.a.position.y, joint.b.position.x, joint.b.position.y, arcade.color.WHITE, 3)
        arcade.draw_text(f'Mode: ', 10, 670, arcade.color.BLUE, font_size=30)
        arcade.draw_text(f'Gravity: ', 1310, 670, arcade.color.BLUE, font_size=30)
        self.gravity_sprite.draw()
        self.sprites.draw()
        self.mode_sprite.draw()
    def on_update(self, delta_time):
        space.step(delta_time)

        self.gravity_sprite = self.gravity_sprite = arcade.Sprite(self.gravity_filter.get(self.gravity, self.gravity), scale=.5, center_x=1460, center_y=680)
        self.mode_sprite = arcade.Sprite(self.mode_filter.get(self.mode, self.mode), scale=.4, center_x=160,
                                         center_y=680)
        if self.mouse_pos is not None and self.shape_being_dragged is not None:
            self.shape_being_dragged.shape.body.position = self.mouse_pos[:2]
            self.shape_being_dragged.shape.body.velocity = self.mouse_pos[2] * 20, self.mouse_pos[3] * 20
        if self.gravity == 0:
            space.gravity = 0, -1000
            space.damping = 1
        elif self.gravity == 1:
            space.gravity = 0, 0
            space.damping = 1
        elif self.gravity == 3:
            space.gravity = -1000, 0
            space.damping = 1
        elif self.gravity == 4:
            space.gravity = 1000, 0
            space.damping = 1
        elif self.gravity == 2:
            space.gravity = 0, 1000
            space.damping = 1
        else:
            space.gravity = 0, 0
            space.damping = 0
        for index, sprite in enumerate(self.sprites):
            sprite.angle = degrees(space.bodies[index].angle)
            sprite.set_position(space.bodies[index].position.x, space.bodies[index].position.y)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.shape_being_dragged = None
            self.mouse_pos = None
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.shape_being_dragged is not None:
            self.mouse_pos = x, y, dx, dy
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 65361:
            self.mode-=1
            if self.mode == -1:
                self.mode = 6
        if symbol == 65363:
            self.mode+=1
            if self.mode == 7:
                self.mode = 0
        if symbol == 65362:
            self.gravity += 1
            if self.gravity == 6:
                self.gravity = 0
        if symbol == 65364:
            self.gravity -= 1
            if self.gravity == -1:
                self.gravity = 5
    def get_shape(self, x, y):
        shape_list = space.point_query((x, y), 1, pymunk.ShapeFilter())

        if len(shape_list) > 0:
            shape = shape_list[0]
        else:
            shape = None
        return shape
    def on_mouse_press(self, x, y, button, modifiers):
        if button == 4:
            if self.mode == 5:
                shape_selected = self.get_shape(x, y)
                if not shape_selected is None:
                    if self.shape_1 is None:
                        self.shape_1 = shape_selected
                        joint = pymunk.SimpleMotor(space.static_body, self.shape_1.shape.body, -50)
                        space.add(joint)
                        self.shape_1 = None
                        self.shape_2 = None
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.mode == 1:
                self.last_mouse_position = x, y
                shape = self.get_shape(x, y)

                if shape is not None:
                    self.shape_being_dragged = shape
            elif self.mode == 0:
                circle_moment = pymunk.moment_for_circle(mass, 0, radius)
                circle_body = pymunk.Body(mass, circle_moment)
                circle_body.position = x, y
                circle_shape = pymunk.Circle(circle_body, radius)
                circle_shape.elasticity = 0.8
                circle_shape.friction = 1.0
                space.add(circle_body, circle_shape)

                self.sprites.append(arcade.Sprite(self.mode_filter[0], center_x=circle_body.position.x, center_y=circle_body.position.y, scale = .4))
            elif self.mode == 2:
                size = 45
                mass_sq = 20.0
                moment = pymunk.moment_for_box(mass_sq, (size, size))
                body = pymunk.Body(mass_sq, moment)
                body.position = pymunk.Vec2d(x, y)
                shape = pymunk.Poly.create_box(body, (size, size))
                shape.friction = 10000
                shape.elasticity = .1
                space.add(body, shape)

                sprite = BoxSprite(shape, self.mode_filter[2], width=size, height=size)
                self.sprites.append(sprite)
            elif self.mode == 3:
                shape_selected = self.get_shape(x, y)
                if not shape_selected is None:
                    if self.shape_1 is None:
                        self.shape_1 = shape_selected
                    elif self.shape_2 is None:
                        self.shape_2 = shape_selected
                        joint = pymunk.PinJoint(self.shape_1.shape.body, self.shape_2.shape.body)
                        space.add(joint)
                        joint.collide_bodies = 0
                        self.joints.append(joint)
                        self.shape_1 = None
                        self.shape_2 = None
            elif self.mode == 4:
                shape_selected = self.get_shape(x, y)
                if not shape_selected is None:
                    if self.shape_1 is None:
                        self.shape_1 = shape_selected
                    elif self.shape_2 is None:
                        self.shape_2 = shape_selected
                        joint = pymunk.DampedSpring(self.shape_1.shape.body, self.shape_2.shape.body, (0, 0), (0, 0), 45, 300, 30)
                        space.add(joint)
                        self.joints.append(joint)
                        self.shape_1 = None
                        self.shape_2 = None
            elif self.mode == 5:
                shape_selected = self.get_shape(x, y)
                if not shape_selected is None:
                    if self.shape_1 is None:
                        self.shape_1 = shape_selected
                        motor = pymunk.SimpleMotor(space.static_body, self.shape_1.shape.body, 50)
                        space.add(motor)
                        self.shape_1 = None
                        self.shape_2 = None
            elif self.mode == 6:
                if self.shape_1 is None:
                    self.shape_1 = x, y
                elif self.shape_2 is None:
                    self.shape_2 = x, y
                    joint = pymunk.Segment(space.static_body, self.shape_1, self.shape_2, 5)
                    joint.friction = 2
                    joint.elasticity = el
                    space.add(joint)
                    seg.append(joint)
                    self.shape_1 = None
                    self.shape_2 = None

MyGameWindow(1480, 720, 'My game window')
arcade.run()