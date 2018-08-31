from InstaUnfollower import InstagramUnfollower

def main():

    username = "ozanyurtsever95@gmail.com"
    password = "OZANMOZAN"

    unfollower = InstagramUnfollower(username,password, 3) #just increase the number to unfollow slower, and decrease to unfollow faster. ( Making too fast may possible shows you as a bot to Instagram )
    unfollower.login() #logins your account
    unfollower.find_username() #finds the username of your account
    unfollower.find_target_users() #finds the target users who we want to unfollow
    unfollower.unfollow_target_users() #unfollows the target users who we determined before

if __name__ == "__main__":
    main()

