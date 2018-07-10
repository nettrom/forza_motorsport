#!/usr/env/python
# -*- coding: utf-8 -*-
'''
Python class for Forza Motorsport 7's data stream format.

Copyright (c) 2018 Morten Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from struct import unpack

## Documentation of the packet format is available on
## https://forums.forzamotorsport.net/turn10_postsm926839_Forza-Motorsport-7--Data-Out--feature-details.aspx#post_926839

class ForzaDataPacket:
    def __init__(self, data):
        ## Format string that allows unpack to process the data bytestream:
        forza_format = '<iIfffffffffffffffffffffffffffffffffffffffffffffffffffiiiii'
        self._parameter_list = [
            'is_race_on', 'timestamp_ms',
            'engine_max_rpm', 'engine_idle_rpm', 'current_engine_rpm',
            'acceleration_x', 'acceleration_y', 'acceleration_z',
            'velocity_x', 'velocity_y', 'velocity_z',
            'angular_velocity_x', 'angular_velocity_y', 'angular_velocity_z',
            'yaw', 'pitch', 'roll',
            'norm_suspension_travel_FL', 'norm_suspension_travel_FR',
            'norm_suspension_travel_RL', 'norm_suspension_travel_RR',
            'tire_slip_ratio_FL', 'tire_slip_ratio_FR',
            'tire_slip_ratio_RL', 'tire_slip_ratio_RR',
            'wheel_rotation_speed_FL', 'wheel_rotation_speed_FR',
            'wheel_rotation_speed_RL', 'wheel_rotation_speed_RR',
            'wheel_on_rumble_strip_FL', 'wheel_on_rumble_strip_FR',
            'wheel_on_rumble_strip_RL', 'wheel_on_rumble_strip_RR',
            'wheel_in_puddle_FL', 'wheel_in_puddle_FR',
            'wheel_in_puddle_RL', 'wheel_in_puddle_RR',
            'surface_rumble_FL', 'surface_rumble_FR',
            'surface_rumble_RL', 'surface_rumble_RR',
            'tire_slip_angle_FL', 'tire_slip_angle_FR',
            'tire_slip_angle_RL', 'tire_slip_angle_RR',
            'tire_combined_slip_FL', 'tire_combined_slip_FR',
            'tire_combined_slip_RL', 'tire_combined_slip_RR',
            'suspension_travel_meters_FL', 'suspension_travel_meters_FR',
            'suspension_travel_meters_RL', 'suspension_travel_meters_RR',
            'car_ordinal', 'car_class', 'car_performance_index',
            'drivetrain_type', 'num_cylinders'
            ]
        
        (self.is_race_on, self.timestamp_ms,
         self.engine_max_rpm, self.engine_idle_rpm, self.current_engine_rpm,
         self.acceleration_x, self.acceleration_y, self.acceleration_z,
         self.velocity_x, self.velocity_y, self.velocity_z,
         self.angular_velocity_x, self.angular_velocity_y, self.angular_velocity_z,
         self.yaw, self.pitch, self.roll,
         self.norm_suspension_travel_FL, self.norm_suspension_travel_FR,
         self.norm_suspension_travel_RL, self.norm_suspension_travel_RR,
         self.tire_slip_ratio_FL, self.tire_slip_ratio_FR,
         self.tire_slip_ratio_RL, self.tire_slip_ratio_RR,
         self.wheel_rotation_speed_FL, self.wheel_rotation_speed_FR,
         self.wheel_rotation_speed_RL, self.wheel_rotation_speed_RR,
         self.wheel_on_rumble_strip_FL, self.wheel_on_rumble_strip_FR,
         self.wheel_on_rumble_strip_RL, self.wheel_on_rumble_strip_RR,
         self.wheel_in_puddle_FL, self.wheel_in_puddle_FR,
         self.wheel_in_puddle_RL, self.wheel_in_puddle_RR,
         self.surface_rumble_FL, self.surface_rumble_FR,
         self.surface_rumble_RL, self.surface_rumble_RR,
         self.tire_slip_angle_FL, self.tire_slip_angle_FR,
         self.tire_slip_angle_RL, self.tire_slip_angle_RR,
         self.tire_combined_slip_FL, self.tire_combined_slip_FR,
         self.tire_combined_slip_RL, self.tire_combined_slip_RR,
         self.suspension_travel_meters_FL, self.suspension_travel_meters_FR,
         self.suspension_travel_meters_RL, self.suspension_travel_meters_RR,
         self.car_ordinal, self.car_class, self.car_performance_index,
         self.drivetrain_type, self.num_cylinders) = unpack(forza_format, data)

    def get_tsv_header(self):
        '''
        Return a tab-separated string with the names of all properties in the order defined in the data packet.
        '''
        return('\t'.join(self._parameter_list))
        
    def to_tsv(self):
        '''
        Return a tab-separated values string with all data in the given order.
        All floating point numbers are defined as such to allow for changing
        the number of significant digits if desired.
        '''
        return('{0.is_race_on}\t{0.timestamp_ms}\t{0.engine_max_rpm:f}\t{0.engine_idle_rpm:f}\t{0.current_engine_rpm:f}\t{0.acceleration_x:f}\t{0.acceleration_y:f}\t{0.acceleration_z:f}\t{0.velocity_x:f}\t{0.velocity_y:f}\t{0.velocity_z:f}\t{0.angular_velocity_x:f}\t{0.angular_velocity_y:f}\t{0.angular_velocity_z:f}\t{0.yaw:f}\t{0.pitch:f}\t{0.roll:f}\t{0.norm_suspension_travel_FL:f}\t{0.norm_suspension_travel_FR:f}\t{0.norm_suspension_travel_RL:f}\t{0.norm_suspension_travel_RR:f}\t{0.tire_slip_ratio_FL:f}\t{0.tire_slip_ratio_FR:f}\t{0.tire_slip_ratio_RL:f}\t{0.tire_slip_ratio_RR:f}\t{0.wheel_rotation_speed_FL:f}\t{0.wheel_rotation_speed_FR:f}\t{0.wheel_rotation_speed_RL:f}\t{0.wheel_rotation_speed_RR:f}\t{0.wheel_on_rumble_strip_FL:f}\t{0.wheel_on_rumble_strip_FR:f}\t{0.wheel_on_rumble_strip_RL:f}\t{0.wheel_on_rumble_strip_RR:f}\t{0.wheel_in_puddle_FL:f}\t{0.wheel_in_puddle_FR:f}\t{0.wheel_in_puddle_RL:f}\t{0.wheel_in_puddle_RR:f}\t{0.surface_rumble_FL:f}\t{0.surface_rumble_FR:f}\t{0.surface_rumble_RL:f}\t{0.surface_rumble_RR:f}\t{0.tire_slip_angle_FL:f}\t{0.tire_slip_angle_FR:f}\t{0.tire_slip_angle_RL:f}\t{0.tire_slip_angle_RR:f}\t{0.tire_combined_slip_FL:f}\t{0.tire_combined_slip_FR:f}\t{0.tire_combined_slip_RL:f}\t{0.tire_combined_slip_RR:f}\t{0.suspension_travel_meters_FL:f}\t{0.suspension_travel_meters_FR:f}\t{0.suspension_travel_meters_RL:f}\t{0.suspension_travel_meters_RR:f}\t{0.car_ordinal}\t{0.car_class}\t{0.car_performance_index}\t{0.drivetrain_type}\t{0.num_cylinders}'.format(self))
