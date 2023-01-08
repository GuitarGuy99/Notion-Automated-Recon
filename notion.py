import re
import requests


def make_box_page(box_name, nmap_output):
  # Notion API Token
  TOKEN = "secret_Lvr0IgYzXQP1yrXRAzVmca3DQzG5GefTMZWaBKlg6JQ"
  # Parent page id
  PARENT = "91c253db90d342fe9f7a44419fbe0481"

  url = "https://api.notion.com/v1/pages"

  headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
  }

  code_blocks = []
  chunk_size = 2000
  total_size = len(nmap_output)
  chunks_out = [ nmap_output[i:i+chunk_size] for i in range(0, total_size, chunk_size) ]

  for chunk in chunks_out:
    code_blocks.append({
      "type": "text",
      "text": {
        "content": chunk
      }
    })

  scan_details = []
  find_matches = re.findall(r'^([0-9]+)\/(tcp|udp)\s+([^\s]+)\s+([^\s]+)\s+(.*)$', nmap_output, flags=re.MULTILINE)

  for port, proto, state, service, version in find_matches:
    scan_details.append(f"Found a {service} {version} Server {state} on {proto} {port}")

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
        "rich_text": code_blocks,
        "language":
        "plain text"
      }
    },{
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{
          "type": "text",
          "text": {
            "content": "\n".join(scan_details)
          }
        }]
      }
    }]
  }

  response = requests.post(url, json=payload, headers=headers)

  return response.json()
