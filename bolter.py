import praw

replyText = "DRILL YOUR BOLTER, BROTHER!"

def main(event, context):
    url = event['url']

    reddit = praw.Reddit('bolterbot')
    submission = reddit.submission(url=url)

    # Upvote because effort should be rewarded.
    submission.upvote()

    submission.reply(replyText)


if __name__ == "__main__":
    main()
