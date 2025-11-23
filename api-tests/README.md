# API Automation – Vikunja (11 automated tests)

Automated API testing of the public Vikunja instance  
→ https://try.vikunja.io (open-source todo & project management tool)

### Test Coverage
- User registration & login (positive + negative scenarios)
- Boundary testing: username 3 chars (min) & 250 chars (max)
- Invalid email format, duplicate user, wrong credentials
- Token extraction from login response → automatic usage in subsequent requests
- User info retrieval with valid and invalid Bearer token

### Highlights
- Pre-request script: generates 250-character username
- Test scripts: status code validation + JSON response assertions
- Environment variables: `Base_URL`, `auth_token`

### Tech Stack
- Postman → Newman
- GitHub (ready for CI/CD)

### Run locally (one command)
```bash
npx newman run "https://raw.githubusercontent.com/SergeiOsipov2099/My-Portfolio/main/api-tests/Vikunja_API_Tests.postman_collection.json" --reporters cli,html --reporter-html-export report.html
