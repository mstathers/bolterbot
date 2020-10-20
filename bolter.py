import praw
from praw.exceptions import APIException
import json

replyText = '''DRILL YOUR BOLTER, BROTHER!

Buy a pin vise set on:  
[Amazon.com](https://www.amazon.com/dp/B07FJ6VD2P/)  
[Amazon.ca](https://www.amazon.ca/gp/product/B085NFRRJ2)
'''

def response(message, status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

def main(event, context):
    reddit = praw.Reddit('bolterbot')

    if event['httpMethod'] == "GET":
        url = event['pathParameters']['url']
        submission = reddit.submission(id=url)
    else:
        message = {
            "error": "Please send a GET"
        }
        return response(message, 500)


    print("Post title: {}".format(submission.title))


    # Upvote because effort should be rewarded.
    submission.upvote()

    try:
        comment = submission.reply(replyText)
        if comment:
            message = {
                "link": "https://reddit.com{}".format(comment.permalink)
            }
            return response(message, 200)
        else:
            message = {
                "error": "error"
            }
            return response(message, 500)
    except APIException as e:
            message = {
                "error": str(e) }
            return response(message, 500)



if __name__ == "__main__":
    main()
