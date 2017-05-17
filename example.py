#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

sys.path.append(os.path.join(sys.path[0], 'src'))

from check_status import check_status
from feed_scanner import feed_scanner
from follow_protocol import follow_protocol
from instabot import InstaBot
from unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login="popcornfly10",
    password="c0cac0la",
    like_per_day=3000,
    comments_per_day=1000,
    tag_list=['follow4follow', 'f4f', 'cute', 'love', 'instagood', 'photooftheday', 'beautiful', 'tbt', 'happy', 'cute', 'fashion', 'me'
    , 'picoftheday', 'selfie', 'summer', 'friends', 'instadaily', 'girl', 'fun', 'repost', 'art', 'smile', 'food', 'follow', 'like4like', 'tagsforlikes', 'instalike', 'likeforlike'
    , 'followforfollow', 'l4l', 'followback', 'instafollow', 'likeforfollow', 'likeforlikes', '20likes', 'likeback', 'likes4likes', 'followher',
    'followhim', 'lfl', 'pleasefollow', 'like4follow', 'teamfollowback', 'BTSBBMAs', 'izmirescort', 'PREMIOSMTVMIAW', 'BBMAs'],
    tag_blacklist=['rain', 'thunderstorm'],
    user_blacklist={},
    max_like_for_one_tag=500,
    follow_per_day=1000,
    follow_time=1,
    unfollow_per_day=1000,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['example_user_1', 'example_user_2'])
while True:
    mode = 0
    if mode == 0:
        bot.new_auto_mod()
    else:
        print("Wrong mode!")
