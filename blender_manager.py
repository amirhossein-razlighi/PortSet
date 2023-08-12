import bpy
import os
from math import cos, sin, radians

# Select the main camera of scene
bpy.context.scene.camera = bpy.data.objects["Camera"]

# List different objects present in the scene
objects = [obj.name for obj in bpy.data.objects]

# Move the camera in a 360° circle from its current position in a circle with radius 5 and in each position, find
# The nearest object to camera, set the depth of field to focus on this object and render
# the scene
camera_initial_position = bpy.data.objects["Camera"].location

for i in range(0, 360, 10):
    bpy.data.objects["Camera"].location.x = camera_initial_position.x + 5 * cos(
        radians(i)
    )
    bpy.data.objects["Camera"].location.y = camera_initial_position.y + 5 * sin(
        radians(i)
    )
    bpy.data.objects["Camera"].location.z = camera_initial_position.z
    bpy.data.objects["Camera"].rotation_euler.z = radians(i)
    bpy.context.scene.camera = bpy.data.objects["Camera"]

    # Uncomment if you want to move the sun
    # Move the sun so that it rays in the same direction as the camera
    # bpy.data.objects["Sun"].location.x = bpy.data.objects["Camera"].location.x
    # bpy.data.objects["Sun"].location.y = bpy.data.objects["Camera"].location.y
    # bpy.data.objects["Sun"].location.z = bpy.data.objects["Camera"].location.z + 5
    # bpy.data.objects["Sun"].rotation_euler.z = radians(i)
    # bpy.context.scene.world.light_settings.use_ambient_occlusion = True

    # Find the nearest object to camera
    nearest_object = ""
    nearest_dist = 1000000
    for obj in bpy.data.objects:
        if obj.name != "Camera":
            dist = (obj.location - bpy.data.objects["Camera"].location).length
            if dist < nearest_dist:
                nearest_dist = dist
                nearest_object = obj.name

    # Set the depth of field to focus on the nearest object
    bpy.data.cameras["Camera"].dof.focus_distance = nearest_dist
    bpy.data.cameras["Camera"].dof.use_dof = True
    bpy.data.cameras["Camera"].dof.focus_object = bpy.data.objects[nearest_object]

    # Render the scene
    bpy.context.scene.render.filepath = os.path.expanduser(
        os.path.join(
            "~/Downloads", "rendered_images", "rendered_image_" + str(i) + ".png"
        )
    )
    bpy.ops.render.render(write_still=True)

# Reset the camera to its initial position
bpy.data.objects["Camera"].location = camera_initial_position
bpy.data.objects["Camera"].rotation_euler.z = 0
bpy.context.scene.camera = bpy.data.objects["Camera"]
