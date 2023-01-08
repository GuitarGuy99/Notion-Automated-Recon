import requests


def make_box_page(box_name, nmap_output):
  # Notion API Token
  TOKEN = "{NOTION_API_KEY_HERE}"
  # Parent page id
  PARENT = "{PARENT_ID_OF_NOTION_PAGE_HERE}"

  url = "https://api.notion.com/v1/pages"

  headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
  }

  payload = {
    "parent": {
      "type": "page_id",
      "page_id": PARENT,
    },
    "properties": {
      "title": {
        "id":
        "title",
        "type":
        "title",
        "title": [{
          "type": "text",
          "text": {
            "content": box_name
          },
          "plain_text": box_name
        }]
      }
    },
    "children": [{
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{
          "type": "text",
          "text": {
            "content": "We start off by running a threader3000/nmap scan..."
          }
        }]
      }
    }, {
      "object": "block",
      "type": "code",
      "code": {
        "rich_text": [{
          "type": "text",
          "text": {
            "content": nmap_output
          }
        }],
        "language":
        "plain text"
      }
    }]
  }

  response = requests.post(url, json=payload, headers=headers)

  return response.json()
