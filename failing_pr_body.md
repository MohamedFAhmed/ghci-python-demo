This PR intentionally changes the `/health` response from `"ok"` to `"okay"`.

**What**
- Modify the JSON returned by `/health`

**Why**
- Teaching demo for reading CI failures

**Expected CI result**
- The test `test_health_route_returns_ok` should fail with an assertion error

**Discussion prompts**
- Where exactly did the failure happen (file and line)?
- What is the **smallest** change that would make the test pass?
