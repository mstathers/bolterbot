import praw

replyText = "DRILL YOUR BOLTER, BROTHER!"

egUrl = 'https://www.reddit.com/r/testingground4bots/comments/dfap5k/can_you_guys_comment_bot_like_stuff_im_testing_a/'

def main():
    reddit = praw.Reddit('bolterbot')
    submission = reddit.submission(url=egUrl)

    # Upvote because effort should be rewarded.
    submission.upvote()

    submission.reply(replyText)


if __name__ == "__main__":
    main()
