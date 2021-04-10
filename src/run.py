#!/usr/bin/env python
"""
    Created by howie.hu at 2021/4/10.
    Description：统一调度入口
    暂定时间：每日的
        - 07:10
        - 11:10
        - 13:10
        - 16:10
        - 20:10
        - 23:10
    Changelog: all notable changes to this file will be documented
"""
import time

import schedule

from src.schedule_task.all_tasks import update_ads_tag, update_wechat_doc


def schedule_task():
    """
    更新持久化订阅的公众号最新文章
    :return:
    """
    # 抓取最新的文章，然后持久化到数据库
    update_wechat_doc()
    # 更新广告标签
    update_ads_tag()


if __name__ == "__main__":
    # 每日抓取公众号最新文章并更新广告标签
    schedule.every().day.at("07:10").do(schedule_task)
    schedule.every().day.at("11:10").do(schedule_task)
    schedule.every().day.at("16:10").do(schedule_task)
    schedule.every().day.at("20:10").do(schedule_task)
    schedule.every().day.at("23:10").do(schedule_task)
    while True:
        schedule.run_pending()
        time.sleep(1)