# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/14 16:59
@file: adb_util.py
@desc: adb命令封装
"""
import os
import re


def get_devices_info(devices_uuid):
    # 获取多设备信息
    devices_info = []
    cmd1 = 'adb -s {} shell getprop ro.product.model'
    cmd2 = 'adb -s {} shell getprop ro.build.version.release'
    if devices_uuid:
        for de in devices_uuid:
            device_model = os.popen(cmd1.format(de)).read()
            device_os_version = os.popen(cmd2.format(de)).read()
            devices_info.append((de, device_model.strip('\n'), device_os_version.strip('\n')))
    return devices_info


class AdbUtil:

    def get_devices(self):
        """
        获取第一个设备的devices_id
        :return:
        """
        cmd = "adb devices"
        reslut = os.popen(cmd).readlines()[1:]
        for item in reslut:
            if item != "\n":
                return str(item).split("\t")[0]

    def get_devices_version(self):
        """
        获取单个系统版本号
        :return:
        """
        cmd1 = 'adb shell getprop ro.build.version.release'
        deviceAndroidVersion = list(os.popen(cmd1).readlines())
        deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
        return deviceVersion

    # 获取测试的包的package
    def get_app_package(self, apk_path):
        appLocation = apk_path
        if os.path.exists(appLocation):
            appPackageAdb = list(os.popen('aapt dump badging ' + appLocation).readlines())
            appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0])[0]
            return appPackage
