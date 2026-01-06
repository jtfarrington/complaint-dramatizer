# complaint-dramatizer
Turn your mundane complaints into Shakespearean prose. 

https://jtfarrington.github.io/complaint-dramatizer/

## Description

Has your coffee gone cold? Did you stub your toe on the bedframe this morning? Finally we can express these tragedies with the emotion they deserve! This web application takes your everyday complaints and transforms them into overly dramatic, theatrical Shakespearean language using Claude AI.

## Screenshot



## Features

- Transform complaints into dramatic Shakespearean prose
- Secure backend API handling
- Clean, simple interface
- Real-time dramatization

## Tech Stack

- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Backend:** Python Flask
- **AI:** Anthropic Claude API (Sonnet 4)

## Live Application

Visit the live app: [https://jtfarrington.github.io/complaint-dramatizer/](https://jtfarrington.github.io/complaint-dramatizer/)

No setup required - just visit and start dramatizing!

## Local Development Setup

Want to run this locally or contribute? Follow these steps:

### Prerequisites

- Python 3.8 or higher
- An Anthropic API key ([Get one here](https://console.anthropic.com/))
- Git

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/complaint-dramatizer.git
cd complaint-dramatizer
```

### 2. Set up Python virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r backend/requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your_api_key_here
```

### 5. Run the backend locally
```bash
cd backend
python app.py
```

The Flask server will start on `http://127.0.0.1:5000`

### 6. Update frontend for local development

In `index.html`, change the API URL to:
```javascript
const response = await fetch('http://127.0.0.1:5000/api/dramatize', {
```

### 7. Open the frontend

Open `index.html` in your web browser.

## Usage

1. Visit the live site or run locally
2. Type your complaint in the text area
3. Click "Dramatize My Complaint"
4. Watch your mundane grievance transform into theatrical prose!

**Keyboard shortcut:** Press `Ctrl+Enter` in the text area to dramatize.

## API Endpoints

### `POST /api/dramatize`
Transforms a complaint into Shakespearean prose.

**Request:**
```json
{
  "complaint": "my toast burned"
}
```

**Response:**
```json
{
  "dramatic_text": "O wretched fate! The bread of mine breakfast..."
}
```

### `GET /api/health`
Health check endpoint.

**Response:**
```json
{
  "status": "ok",
  "message": "Backend is running!"
}
```

## Rate Limiting

To protect API costs and prevent abuse, the backend implements rate limiting:

- **Global limits:** 100 requests per day, 20 per hour per IP
- **Endpoint limit:** 10 requests per minute to `/api/dramatize`
- Exceeded limits return a dramatic error message

## Deployment

### Backend (Render)

The backend is deployed on Render's free tier:
- Automatic deploys from `main` branch
- Environment variables set in Render dashboard
- Uses Gunicorn as production server

### Frontend (GitHub Pages)

The frontend is hosted on GitHub Pages:
- Automatic deploys when pushing to `main` branch
- Serves static HTML/CSS/JS
- Updates within 1-2 minutes of push

## Cost Considerations

- **Backend hosting:** Free tier on Render
- **Frontend hosting:** Free on GitHub Pages
- **API calls:** Uses prepaid Anthropic credits
- **Rate limiting:** Protects against excessive API usage
- Suitable for personal use and moderate traffic

## Security Notes

-  API key stored in environment variables (never in code)
-  `.env` file excluded from version control
-  Rate limiting prevents abuse
-  CORS configured for production
-  Current CORS allows all origins (consider restricting for production)

## Future Improvements

-  Add copy-to-clipboard button
-  Multiple drama styles (Victorian, Gothic, Soap Opera)
-  History of past dramatizations with local storage
-  Mobile-responsive design improvements
-  User preferences for output length/style
-  Stricter CORS configuration

## Contributing

This is a learning project, but feel free to fork and experiment! Pull requests welcome.

## License

MIT License - feel free to use this project however you'd like!

## Acknowledgments

- Built with [Anthropic's Claude API](https://www.anthropic.com/)
- Created as a learning project to explore Flask, APIs, and full-stack deployment
- Deployed on [Render](https://render.com/) and [GitHub Pages](https://pages.github.com/)

## Links

- **Live App:** [https://jtfarrington.github.io/complaint-dramatizer/](https://jtfarrington.github.io/complaint-dramatizer/)
- **Backend API:** [https://complaint-dramatizer-backend.onrender.com](https://complaint-dramatizer-backend.onrender.com)
- **Repository:** [https://github.com/jtfarrington/complaint-dramatizer](https://github.com/jtfarrington/complaint-dramatizer)

---

*"To complain, or not to complain—that is never the question, for we shall always complain most spectacularly"*