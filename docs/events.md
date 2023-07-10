# NoneFly Event List

## Summary

* [ ] BaseEvent
  * [ ] ActionEvent
    * [ ] ActionSuccess
    * [ ] ActionWorking
    * [ ] ActionFailed
  * [ ] NotifyEvent
    * [ ] ErrorNotify
    * [ ] LogNotify

## WebSocket API

> Received by client

Message structure:

```json
{
    "token": "...",
    "event": "{event_name}",
    "params": {
        "key...": "value..."
    }
}
```
