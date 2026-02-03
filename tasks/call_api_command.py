import hashlib
import hmac
import json
import http.client
import os
from datetime import datetime, timezone

from tasks.base.command import Command

NAME = os.environ.get("USER_NAME",'test')
EMAIL = os.environ.get("USER_EMAIL",'test')
RESUME_LINK = os.environ.get("CV_LINK",'test')
REPO_LINK = os.environ.get("REPO_LINK",'test')
SECRET = os.environ.get("SECRET",'test')
RUN_ID = os.environ.get("RUN_ID",'test')


class CallAPICommand(Command):
    def __init__(self, args=None):
        Command.__init__(self, 'call-api', args)

    def execute(self):
        conn = http.client.HTTPSConnection("b12.io")
        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        payload_dict = {
            "timestamp": timestamp,
            "name": NAME,
            "email": EMAIL,
            "resume_link": RESUME_LINK,
            "repository_link": REPO_LINK,
            "action_run_link": f"{REPO_LINK}/actions/runs/{RUN_ID}"
        }
        payload = json.dumps(payload_dict, separators=(',', ':'), sort_keys=True)
        signature = hmac.new(
            key=SECRET.encode("utf-8"),
            msg=payload.encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()
        headers = {
            "Content-Type": "application/json",
            "X-Signature-256": f"sha256={signature}"
        }
        conn.request("POST", "/apply/submission", payload, headers)
        res = conn.getresponse()
        data = res.read()
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                f.write(f"result={data}\n")
        else:
            print(data)
