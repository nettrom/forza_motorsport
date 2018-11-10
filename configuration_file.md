The data out format in Forza Motorsport 7 contains a wide variety of parameters. Some of those may or may not be very informative at any given point in time. To facilitate logging only the data you want, the `data2file.py` utility can read in a configuration file that specifies the parameters you're interested in.

This document describes how to write that configuration file, and gives a list of all the data that can be logged. I've also created an example configuration file with a short list of parameters in `example_configuration.yaml`.

The configuration file needs to be written in a language called YAML. It is not a very complicated language, and the configuration file is a text file, meaning it can be edited with common text editors like Notepad on Windows and TextEdit on Mac OS.

In the case of `data2file.py`, the configuration file will consist of either lines looking like `key: value` that specify an option and it's value, or the list of parameters. We will cover the latter in more detail below.

## Configuration options
The configuration file can override all the command line options. They are as follows:

* `port`: The port number of listen on. Needs to be a number, typically larger than 1024.
** Example: `port: 1123`
* `output_filename`: The name of the file to write the logged data to.
** Example: `output_filename: forza_data.tsv`
* `format`: The format of the output file, one of either `tsv` (tab-separated values) or `csv` (comma-separated values).
** Example: `format: tsv`
* 'append': Whether the data should be appended to the output file, or if the file should be created/overwritten. The value should be either `True` or `False`, respectively.
** Example: `append: False`
* `packet_format`: The format of the data packets. Either `sled`, the older format, or `dash`, the newer format.
** Example: `packet_format: dash`

The example configuration file sets all of these options and can be used as a starting point for creating your own configuration file.

## List of parameters
Perhaps the most useful part of the configuration file is the possibility of specifying what data should be logged. By default, everything is logged, and it's a fairly large amount of data. That's not very useful if only a few of the things really interests you.

In the configuration file the parameter list is its own option, so the first line of it has to start with `parameter_list:`. Below that you will write each parameter you want logged on a separate line, indenting it with a few spaces followed by a dash and another space before the parameter's name. Here's an example:

```yaml
parameter_list:
  - lap_no
  - cur_lap_time
  - cur_race_time```

This configuration logs only the current lap number, the current lap time, and the current race time.

Here are all the potential parameters that can be defined. For some of them, we've supplied an explanation of what they are.

* `wall_clock`: the local time when the packet was logged. This parameter is not transmitted by the game, but is instead calculated by the logging script.
* `timestamp_ms`: the game's internal timestamp in milliseconds.
* `engine_max_rpm`: maximum RPM possible of the car's engine.
* `engine_idle_rpm`: idle RPM of the car's engine.
* `current_engine_rpm`: current RPM of the car's engine.
* `acceleration_x`
* `acceleration_y`
* `acceleration_z`
* `velocity_x`
* `velocity_y`
* `velocity_z`
* `angular_velocity_x`
* `angular_velocity_y`
* `angular_velocity_z`
* `yaw`
* `pitch`
* `roll`
* `norm_suspension_travel_FL`: normalized suspension travel of the front left suspension. 0.0 means full stretch, 1.0 means full compression.
* `norm_suspension_travel_FR`: normalized suspension travel of the front right suspension.
* `norm_suspension_travel_RL`: normalized suspension travel of the rear left suspension.
* `norm_suspension_travel_RR`: normalized suspension travel of the rear right suspension.
* `tire_slip_ratio_FL`: tire normalized slip ratio for the front left tire. 0.0 means 100% grip and a ratio above 1.0 means loss of grip.
* `tire_slip_ratio_FR`: tire normalized slip ratio for the front right tire.
* `tire_slip_ratio_RL`: tire normalized slip ratio for the rear left tire.
* `tire_slip_ratio_RR`: tire normalized slip ratio for the rear right tire.
* `wheel_rotation_speed_FL`: wheel rotation speed of the front left tire (in radians per second).
* `wheel_rotation_speed_FR`: wheel rotation speed of the front right tire.
* `wheel_rotation_speed_RL`: wheel rotation speed of the rear left tire.
* `wheel_rotation_speed_RR`: wheel rotation speed of the rear right tire.
* `wheel_on_rumble_strip_FL`: whether the front left tire is on a rumble strip (0 means no, 1 means yes).
* `wheel_on_rumble_strip_FR`: whether the front right tire is on a rumble strip.
* `wheel_on_rumble_strip_RL`: whether the rear left tire is on a rumble strip.
* `wheel_on_rumble_strip_RR`: whether the rear right tire is on a rumble strip.
* `wheel_in_puddle_FL`: whether the front left tire is in a puddle (from 0 to 1, where 1 is the deepest puddle).
* `wheel_in_puddle_FR`: whether the front right tire is in a puddle.
* `wheel_in_puddle_RL`: whether the rear left tire is in a puddle.
* `wheel_in_puddle_RR`: whether the rear right tire is in a puddle.
* `surface_rumble_FL`: non-dimensional surface rumble value for the front left tire (passed to controller force feedback).
* `surface_rumble_FR`: non-dimensional surface rumble value for the front right tire.
* `surface_rumble_RL`: non-dimensional surface rumble value for the rear left tire
* `surface_rumble_RR`: non-dimensional surface rumble value for the rear right tire.
* `tire_slip_angle_FL`: normalized slip angle for the front left tire (0 means 100% grip, and angle above 1.0 means loss of grip).
* `tire_slip_angle_FR`: normalized slip angle for the front right tire.
* `tire_slip_angle_RL`: normalized slip angle for the rear left tire.
* 'tire_slip_angle_RR`: normalized slip angle for the rear right tire.
* `tire_combined_slip_FL`: normalized combined slip for the front left tire (0 means 100% grip, and slip above 1.0 means loss of grip).
* `tire_combined_slip_FR`: normalized combined slip for the front right tire.
* `tire_combined_slip_RL`: normalized combined slip for the rear left tire.
* `tire_combined_slip_RR`: normalized combined slip for the rear right tire.
* `suspension_travel_meters_FL`: actual suspension travel in meters for the front left suspension.
* `suspension_travel_meters_FR`: actual suspension travel in meters for the front right suspension.
* `suspension_travel_meters_RL`: actual suspension travel in meters for the rear left suspension.
* `suspension_travel_meters_RR`: actual suspension travel in meters for the rear right suspension.
* `car_ordinal`: unique identifier of the car make and model.
* `car_class`: car class from 0 (D class) to 7 (X class), inclusive.
* `car_performance_index`: performance index (PI) of the car, from 100 (slowest) to 999 (fastest), inclusive.
* `drivetrain_type`: drivetrain type of the car; 0 = front-wheel drive, 1 = rear-wheel drive, 2 = all-wheel drive.
* `num_cylinders`: number of cylinders in the engine
* `position_x`: position of the car in meters.
* `position_y`: position of the car in meters.
* `position_z`: position of the car in meters.
* `speed`: current speed in meters per second.
* `power`: current power output of the engine in watts.
* `torque`: current torque of the engine in newton meters.
* `tire_temp_FL`: tire temperature of the front left tire.
* `tire_temp_FR`: tire temperature of the front right tire.
* `tire_temp_RL`: tire temperature of the rear left tire.
* `tire_temp_RR`: tire temperature of the rear right tire.
* `boost`: boost pressure.
* `fuel`: amount of fuel left.
* `dist_traveled`: distance traveled.
* `best_lap_time`: best lap time of the current race/session (in seconds).
* `last_lap_time`: lap time of the previous lap.
* `cur_lap_time`: current time of the current lap.
* `cur_race_time`: current total race time.
* `lap_no`: lap number of the current lap.
* `race_pos`: position in the race.
* `accel`: amount of acceleration input (0-255).
* `brake`: amount of brake input.
* `clutch`: amount of clutch input.
* `handbrake`: amount of handbarke input.
* `gear`: the gear the car is currently in.
* `steer`: the amount of steering input.
* `norm_driving_line`: normalized driving line.
* `norm_ai_brake_diff`: normalized AI brake difference.
