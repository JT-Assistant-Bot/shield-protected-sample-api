# Shield Protected Sample API

## 🔐 Paid Access Required

This API is protected by GlobalAIEnterprise Shield.

All requests require a valid API key.

👉 Purchase access here:
https://jathangkip.gumroad.com/l/vtagec

Requests without a key will be rejected.

This is a deliberately simple API.

It has no security of its own.

Every request is allowed or blocked by an external service:
GlobalAIEnterprise Shield.

If Shield is removed, this API becomes unsafe.

---

## How It Works

Before returning data, this API calls:

```
GET /shield/check
```

If the request is allowed → data is returned  
If blocked → request fails

---

## Why This Exists

This repository demonstrates how GlobalAIEnterprise Shield is used
as a mandatory dependency, not a feature.

Remove the Shield call and you remove protection.
