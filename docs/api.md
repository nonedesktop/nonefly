# NoneFly API List

## Summary

* [ ] status
* [ ] security
  * [ ] history
  * [ ] lock
  * [ ] refresh
* [ ] instance
  * [ ] new
  * [ ] info
  * [ ] run
  * [ ] stop
  * [ ] restart
  * [ ] export
  * [ ] import
  * [ ] remove
* [ ] file
  * [ ] list
  * [ ] pull
  * [ ] push
  * [ ] create
  * [ ] rename
  * [ ] copy
  * [ ] move
  * [ ] delete
* [ ] extension
  * [ ] install
  * [ ] uninstall
  * [ ] enable
  * [ ] disable

## Simple API

> Prefix: `/nonefly/simple`

For 1-level API:

```plaintext
/nonefly/simple/{lv1_api}
```

For 2-level API:

```plaintext
/nonefly/simple/{lv1_api}/{lv2_api}
```

## WebSocket API

> Endpoint: `/nonefly/ws`

Message structure:

```json
{
    "token": "...",
    "api": "{lv1_api}.{lv2_api}",
    "opid": "...",
    "params": {
        "key...": "value..."
    }
}
```
