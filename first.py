from slackclient import SlackClient

token = "xoxp-76525183170-76515208005-76525910626-3cf0eb4c95"      # found at https://api.slack.com/web#authentication
sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("channels.info", channel="1234567890")
print sc.api_call(
        "chat.postMessage", channel="#job", text="Hello from Python! :tada:",
        username='admin', icon_emoji=':robot_face:'
)

