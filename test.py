import os 
import time
import string, random
import uiautomator2 as u2

# dir_path = os.path.dirname(os.path.realpath(__file__))
# working_dir = os.getcwd()
# print(dir_path, working_dir)

#print(gmapi2.get_instagram_ver_code_guerillamail('EtHhiw6ZVRJWW'))



# d = u2.connect('R38MB0F4XDF') # connect to device
# d.app_start("com.instagram.android")
# # # time.sleep(5)  # w
# # #d.screenshot("app-launched.jpg")

# print(d.info)
# # # # d.open_url("instagram://instagram.com")
# # # # xml = d.dump_hierarchy()
# # # # with open('a.txt', 'w',encoding="utf-8") as f:
# # # #     f.write(xml)
# # # #.click(690, 90)
# # # #(text="sonshinegod", instance=1).click()
def go_to_create_account(emulator):
#   #android.widget.FrameLayout
    d = u2.connect(emulator) # connect to device
    d.open_quick_settings()
    time.sleep(2)
    xml = d.dump_hierarchy()
    with open('xen', 'w',encoding="utf-8") as f:
        f.write(xml) 
    d(resourceId="com.android.systemui:id/settings_button_container").click()
    
    #resourceId="com.android.systemui:id/settings_button_container"
    c=445
    time.sleep(2)
    d(text="Google",resourceId="android:id/title").click()
    time.sleep(2)
    xml = d.dump_hierarchy()
    if 'resource-id="com.google.android.gms:id/og_selected_account_disc_apd"' in xml:
        d(resourceId="com.google.android.gms:id/og_selected_account_disc_apd").click()
        d(text="Add another account", resourceId="com.google.android.gms:id/og_text_card_title").click()
    else:    
        d(resourceId="Card: Sign in").click()
    #<node index="0" text="" resource-id="Card: Sign in" class="android.view.View" package="com.google.android.gms" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[56,1030][1384,1504]" drawing-order="0" hint="" display-id="0">

    # while True:
    #     #d.click(0.5, c)
    #     try:
    #         d(text="scdvds vsvs", className="android.widget.TextView").send_keys('test')
    #     except:
    
    #         continue
    #     else:
    #         break
    time.sleep(2)

    # d.push(fr'moved.jpg', '/images/')
    # d.du
    #d.app_start("com.instagram.android")
    width, height = d.window_size()
def create_account(emulator):
    d = u2.connect(emulator) # connect to device
    time.sleep(2)
    d.screenshot("gss2.jpg")

    # xml = d.dump_hierarchy()
    # time.sleep(2)
    # with open('GSSxs', 'w',encoding="utf-8") as f:
    #     f.write(xml) 
    # username =''.join(random.choice(string.ascii_uppercase +string.ascii_lowercase+ string.digits) for _ in range(13))
    # password=  ''.join(random.choice(string.ascii_uppercase +string.ascii_lowercase+ string.digits) for _ in range(13))
    # time.sleep(5)
    # while True:
    #     d(text="Create account", className="android.widget.Button").click()

    #     try:
    #         d(text="For work or my business", className="android.view.MenuItem").click()
    #     except:
    #         continue
    #     else:
    #         break
    #d(className="android.widget.EditText").send_keys('sdssfs')
    #d(text="Create account", className="android.widget.Button").click()
    # d(text="For work or my business", className="android.view.MenuItem").click()
    # d(resourceId="firstName",className="android.widget.EditText").send_keys('Name')
    # #d(resourceId="lastName",className="android.widget.EditText").send_keys('Lame')
    # #<node NAF="true" index="2" text="" resource-id="firstName" class="android.widget.EditText" package="com.google.android.gms" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[65,569][1013,711]" drawing-order="0" hint="First name" display-id="0" />
    # time.sleep(2)
    # xml = d.dump_hierarchy()
    # if "'Try out your stylus'" in xml:
    #     d(text="Cancel",resourceId="android:id/closeButton").click()
    #     d(text="NEXT", className="android.widget.Button").click()
    # try:
    #     d(text="NEXT", className="android.widget.Button").click()
    #     print('button clicked')
    # except Exception as e:
    #     print(e)
    #     try:
    #         d.click(0.5, 0.5)
    #         d(text="NEXT", className="android.widget.Button").click()
    #     except:
    #         time.sleep(1)
            

    # time.sleep(2)
#text="Cancel" resource-id="android:id/closeButton"
    # while True:
    #     d(text="NEXT", className="android.widget.Button").click()
    #     try:
    #         d(text="For work or my business", className="android.view.MenuItem").click()
    #     except:
    #         continue
    #     else:
    #         break
    # time.sleep(2)
   
    # s
    # if "Username" in xml:
#     d(resourceId="month").click()
#     d(text="January",resourceId="android:id/text1").click()
#     d(resourceId="day").send_keys('20')
#     d(resourceId="year").send_keys('2000')
#     d(resourceId="gender").click()
#     d(text="Male",resourceId="android:id/text1").click()
#     d(text="NEXT", className="android.widget.Button").click()
#     time.sleep(3)
#     xml = d.dump_hierarchy()
#     if 'hint="Username"'in xml: 
#         d(className="android.widget.EditText").send_keys(username)
#         print('username: '+ username)
#     else:
#         d(className="android.widget.RadioButton").click()
    
#     d(text="NEXT", className="android.widget.Button").click()
#     d.screenshot("gss0.jpg")
#     time.sleep(2)
#     d(className="android.widget.EditText").send_keys(password)
#     time.sleep(3)
#     d.screenshot("gss2.jpg")
#     d(text="NEXT", className="android.widget.Button").click()
#     d.screenshot("gss3.jpg")
#     # if review account, click next
#     d(text="NEXT", className="android.widget.Button").click()
#     d(scrollable=True).scroll.toEnd(steps=3)
#     d(text="I agree", className="android.wid    get.Button").click()
# #<node index="46" text="I agree" resource-id="" class="android.widget.Button" package="com.google.android.gms" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[769,2173][1018,2273]" drawing-order="0" hint="" display-id="0" />
#     d(className="android.widget.Button").click()
#     d(scrollable=True).scroll.toEnd(steps=3)
#     d(text="I agree", className="android.widget.Button").click()
#     with open('google-accounts.txt', 'a+',encoding="utf-8") as f:
#         f.write(f'{username+'@gmail.com'}:{password}') 

#                          <node index="4" text="Confirm" resource-id="" class="android.widget.Button" package="com.google.android.gms" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="true" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[787,1417][976,1514]" drawing-order="0" hint="" display-id="0" />



    #<node index="0" text="January" resource-id="android:id/text1" class="android.widget.CheckedTextView" package="com.google.android.gms" content-desc="" checkable="true" checked="false" clickable="true" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[70,303][1010,450]" drawing-order="1" hint="" display-id="0" />

    #  <node index="2" text="Month" resource-id="month" class="android.view.View" package="com.google.android.gms" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[63,564][354,714]" drawing-order="0" hint="" display-id="0" />

    #<node NAF="true" index="3" text="" resource-id="day" class="android.widget.EditText" package="com.google.android.gms" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[396,567][685,714]" drawing-order="0" hint="Day" display-id="0" />

    #<node NAF="true" index="4" text="" resource-id="year" class="android.widget.EditText" package="com.google.android.gms" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[727,567][1015,714]" drawing-order="0" hint="Year" display-id="0" />

    #<node index="5" text="Gender" resource-id="gender" class="android.view.View" package="com.google.android.gms" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[63,753][1018,903]" drawing-order="0" hint="" display-id="0" /
#text="For work or my business" resource-id="" class="android.view.MenuItem" package="com.google.android.gms" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[39,1367][590,1498]" drawing-order="0" hint="" display-id="0" />
    
    # # # #for i in range(0, 2)
    # xml = d.dump_hierarchy()
    # time.sleep(2)
    # with open('vsg3XssSx1.txt', 'w',encoding="utf-8") as f:
    #     f.write(xml) 
    # time.sleep(2)
    # click profile
    #d.long_click(width - 50, 1400) 
emulator='emulator-5554' 
# go_to_create_account(emulator)
create_account(emulator)
  
# d = u2.connect(emulator) # connect to device
# xml = d.dump_hierarchy()
# with open('xen22', 'w',encoding="utf-8") as f:
#     f.write(xml) 
# d(text="NEXT", className="android.widget.Button").click()
def logout():
    d = u2.connect('R38MB0F4XDF') # connect to device

    d.app_start("com.instagram.android")
    width, height = d.window_size()
    #d.click(width - 90, 1400) 
    #d.click(width - 90, 1400)  
    d.click(width - 110, 1400)
    time.sleep(2)

    d.click(width - 100, 100)  
    time.sleep(2)
    d(scrollable=True).scroll.toEnd(steps=4)
    d(text='Log out', className='android.widget.Button').click()
    time.sleep(2)
    d(text='Log out', className='android.widget.Button').click()



    xml = d.dump_hierarchy()
    with open('ann1.txt', 'w',encoding="utf-8") as f:
        f.write(xml) 
def script():
    d = u2.connect('R38MB0F4XDF') # connect to device
    # d.push(fr'moved.jpg', '/images/')
    # d.du
    d.app_start("com.instagram.android")
    xml = d.dump_hierarchy()
    with open('ann1234x.txt', 'w',encoding="utf-8") as f:
        f.write(xml) 
    d(resourceId="com.instagram.android:id/search_tab").click()
    d(resourceId="com.instagram.android:id/action_bar_search_hints_text_layout").click()
    d.send_keys('epica', clear=True)
    d(resourceId="com.instagram.android:id/row_search_user_username").click()
    time.sleep(2)
    xml = d.dump_hierarchy()
    with open('veel.txt', 'w',encoding="utf-8") as f:
        f.write(xml) 
    #d(resourceId="com.instagram.android:id/clips_swipe_refresh_container").click()
    #d(text="Follow", resourceId="com.instagram.android:id/profile_header_follow_button").click()
    
    time.sleep(4)
    
    d(scrollable=True).scroll(steps=2)
    time.sleep(2)
    d.click(0.5, 1200)
    # time.sleep(500)
    #<node index="0" text="" resource-id="com.instagram.android:id/root_clips_layout" class="android.widget.LinearLayout" package="com.instagram.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[0,57][720,1340]" drawing-order="1" hint="" display-id="0">

        #   <node index="0" text="" resource-id="com.instagram.android:id/gesture_manager" class="android.widget.FrameLayout" package="com.instagram.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[0,57][720,1340]" drawing-order="1" hint="" display-id="0">

        #     <node index="0" text="" resource-id="com.instagram.android:id/clips_swipe_refresh_container" class="android.view.ViewGroup" package="com.instagram.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[0,57][720,1340]" drawing-order="1" hint="" display-id="0">

        #       <node index="0" text="" resource-id="com.instagram.android:id/clips_viewer_view_pager" class="androidx.viewpager.widget.ViewPager" package="com.instagram.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="true" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[0,57][720,1340]" drawing-order="1" hint="" display-id="0">

    time.sleep(4)
    xml = d.dump_hierarchy()
    with open('ve.txt', 'w',encoding="utf-8") as f:
        f.write(xml) 

    d(resourceId="com.instagram.android:id/search_tab").click()
    d(resourceId="com.instagram.android:id/action_bar_search_hints_text_layout").click()
    d.send_keys('gibsonguitarnl', clear=True)
    d(resourceId="com.instagram.android:id/row_search_user_username").click()
    #d(text="Follow", resourceId="com.instagram.android:id/profile_header_follow_button").click()


    #                                        <node index="0" text="Follow" resource-id="com.instagram.android:id/profile_header_follow_button" class="android.widget.Button" package="com.instagram.android" content-desc="Follow EPICA" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="true" password="false" selected="true" visible-to-user="true" bounds="[23,618][318,680]" drawing-order="1" hint="" display-id="0" />

    # d(text="Search", resourceId="com.instagram.android:id/action_bar_search_edit_text")
    # d(resourceId="com.sec.android.app.launcher:id/recent_search_bar" ).send_keys('epica')
    #d.send_keys('dd')
    time.sleep(5)
    xml = d.dump_hierarchy()
    with open('ann1234x.txt', 'w',encoding="utf-8") as f:
        f.write(xml) 
    #d(resourceId="com.instagram.android:id/search_tab").send_keys()

# while True:
#     create_account()
#     time.sleep(2)

#     logout()
#     time.sleep(4)
#script()
# click 'skip'
# d = u2.connect('R38MB0F4XDF') # connect to device
# # d.app_start("com.instagram.android")

# width, height = d.window_size()
# width=720
# email_username, email = gmapi2.gen_guerillamail_email()
# login=email
# #click email bt
# # d.click(width-150, 300)  

# time.sleep(2)

# # click email input field
# d.click(width-150, 400)  
# time.sleep(2)

# d.clear_text() 
# d.send_keys(email)

# d.click(0.5, 500)  
# #d.click(0.5, 1300)  


#d.click(width - 50, 100)  

# d.click(0.5, 1300)  

# # click 'skip'
# d.click(width - 50, 100)  


# # click 'next'
# d.click(0.5, 1300)

# time.sleep(2)
# d.screenshot("moved.jpg")
# # d(text="Add Instagram account", instance=0).click()
# # d(text="Create new accounts", instance=0).click()

# d.click(width - 50, 100)  
# d(scrollable=True).scroll.toEnd()
# d(scrollable=True).scroll.toEnd()

# d(scrollable=True).scroll.toEnd()
# d(scrollable=True).scroll.toEnd()
# d(scrollable=True).scroll.toEnd()




# d.long_click(width - 50, 1405)  

# xml = d.dump_hierarchy()
# with open('a.txt', 'w',encoding="utf-8") as f:
#     f.write(xml)    
#     # tap on 'Sign up' or 'Create new account'
#     if d(textContains="Sign up").exists:
#         d(textContains="Sign up").click()
#     elif d(textContains="Create new account").exists:
#         d(textContains="Create new account").click()
#     else:
#         print("could not find sign up button")
#         exit()
#     d.screenshot("2.jpg")

#     time.sleep(3)

#     # enter details - here you can automate entering email or phone
#     if d(text="Email address or phone number").exists:
#         d(text="Email address or phone number").click()
#         d.send_keys("your_email@example.com")  # change to test email/phone
#         d(text="Next").click()
#         time.sleep(2)
    
#     # you may be asked to enter full name and password
#     if d(text="Full name").exists:
#         d(text="Full name").click()
#         d.send_keys("Test User")
    
#     if d(text="Password").exists:
#         d(text="Password").click()
#         d.send_keys("YourSecurePassword123")

#     if d(text="Next").exists:
#         d(text="Next").click()
#         print("submitted sign-up form")

#     # at this point, verification step may appear
#     print("check device for verification steps (e.g., code entry)")
    
# else:
#     print("user is already logged in. please log out to create a new account.")