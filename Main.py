# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-08-31 20:58:46
# @Last modified by:   LC
# @Last Modified time: 2017-03-23 17:20:39
# @Email: liangchaowu5@gmail.com

import time 
import random
from Robot import Robot

from get_proxy_and_user_information.GetProxy import get_valid_proxy 

if __name__ == '__main__':
    # provide the informaion of the product on Amazon, including asin and words for searching
    asin = 'B07BF962T6'
    #asin = 'B002NSMFOQ'
    search_words = 'Leather Women Wallets'
    add_to_cart_probability = 0.7
    while True:
        try:
            proxy = get_valid_proxy('https://www.amazon.com', 'china_ips')
            robot = Robot(proxy)
            ###############################################
            # sign in and browse
            ###############################################
            """
            robot.sign_in()
            # one item
            robot.search_keywords(search_words)
            robot.simulate_browsing(search_words, asin, add_to_cart_probability)
            # another item
            # ....
            """
            ###############################################
            # sign up
            ############################################### 
            #normal sign up
            """
            user_info = robot.generate_sign_up_user(random_password=True)
            robot.sign_up(user_info)
            """
        
            # sign up
            user_info = robot.generate_sign_up_user(random_password=True)
            robot.sign_up(user_info)
            time.sleep(5)
            robot.search_keywords(search_words)
            time.sleep(5)
            robot.simulate_browsing(search_words, asin, add_to_cart_probability)
            robot.exit_driver()
            doc=random.randint(1, 12)
            print 'The system will take a break for %s minutes'%doc
            time.sleep(60*doc)
        except Exception, e:
            print 'Error while exiting the web driver\n%s'%e.message 
            robot.exit_driver()
            doc=random.randint(1, 12)
            print 'The system will take a break for %s minutes'%doc
            time.sleep(60*doc)
            continue