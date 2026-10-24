
# Azerbaijani with Rashida

A responsive, single-page Streamlit website for an Azerbaijani language
teacher and content creator.

The site includes a branded landing page, lesson and culture cards,
a teacher introduction with a replaceable portrait, an interactive
phrase lesson, a three-question quiz, FAQs, and contact options.

## Before public launch

Replace the Instagram URL and email placeholders in `config.py`.
Add Rashida's real portrait if desired. No invented qualifications,
testimonials, prices, or availability are included.

## Features

- Purple-and-yellow visual identity and responsive CSS.
- Navigation links to website sections.
- Three lesson paths and three culture topics.
- Interactive phrase translations and quiz.
- Expandable FAQs.
- Configurable Instagram and email contact links.
- Optional enquiry form that validates input and prepares an email draft.
- No false success message or storage of visitor form submissions.
- Centralized brand and contact configuration.
- Ready for GitHub and Streamlit Community Cloud.

## Project structure

```text
azeri_website/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml
└── assets/
    └── images/
        └── README.md
```

Add Rashida's portrait at
`assets/images/rashida-portrait.jpg`.

## Prerequisites

- Python 3.10 or newer recommended.
- Git, if publishing to GitHub.
- Internet access for installing packages.

## Run locally on Windows

Open PowerShell in the project folder and run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks environment activation, run this in the current
PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

Alternatively, run without activation:

```powershell
.venv\Scripts\python.exe -m streamlit run app.py
```

## Run locally on macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit, usually:

`http://localhost:8501`

Stop the server with `Ctrl+C`.

## Configure contact details

Edit `config.py` and update:

- `instagram_url`: Rashida's real Instagram profile URL.
- `contact_email`: the email address she wants to publish.
- `portrait_path`: path to the approved portrait.
- `website_title`: browser page title.
- Brand color values, if desired.

The contact buttons remain disabled until the placeholder values
are replaced.

The optional contact form prepares a `mailto:` email draft. Visitors
must press Send in their own email app. The site does not transmit
or store form submissions.

If email delivery is added later, use a supported email provider
and keep credentials in Streamlit secrets. Never commit credentials
or private visitor data to GitHub.

## Add or replace images

1. Place an approved portrait at
   `assets/images/rashida-portrait.jpg`.
2. Prefer an optimized JPG or WebP image.
3. If the filename changes, update `portrait_path` in `config.py`.
4. The site displays a placeholder until a real portrait is supplied.

## Publish to GitHub

Create an empty repository on GitHub. Open a terminal in the project
folder and run:

```bash
git init
git add .
git commit -m "Build Azerbaijani with Rashida website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace the example repository URL with your own.

Check the staged files before pushing. The `.gitignore` file excludes
virtual environments, local environment files, secrets, and common
development artifacts.

Never commit `.env`, `.streamlit/secrets.toml`, passwords, API keys,
or private visitor data.

## Deploy to Streamlit Community Cloud

1. Push your project to GitHub.
2. Visit https://share.streamlit.io/.
3. Sign in and connect your GitHub account.
4. Select Create app.
5. Choose your repository and the `main` branch.
6. Set the main file path to `app.py`.
7. Deploy the app.
8. Open the published URL and test the website on desktop and mobile.

Streamlit Community Cloud installs the dependencies in
`requirements.txt`.

If you later add an integration requiring credentials, configure
Secrets in the app settings and access them using `st.secrets`.
No secrets are required for this starter project.

## Update the live website

After testing changes locally, run:

```bash
git add .
git commit -m "Update website"
git push
```

Streamlit Community Cloud normally detects the new commit and
redeploys the app. Check the deployment logs if an update fails.

## SEO notes

The browser title is configured with `st.set_page_config`.
The meta description is stored in `config.py` for future use, but
this implementation does not inject a custom description meta tag.

Streamlit offers less control over traditional SEO metadata and
semantic HTML than a dedicated website framework. Search ranking
is not guaranteed.

## Troubleshooting

- **Streamlit command not found:** activate `.venv`, reinstall
  requirements, or run `python -m streamlit run app.py`.
- **Python version problems:** install Python 3.10 or newer and
  recreate the virtual environment.
- **Contact buttons disabled:** replace the placeholders in
  `config.py` and restart the app.
- **Portrait missing:** check the filename and path.
- **Navigation issues:** test the anchors in your deployed browser.
- **Cloud deployment fails:** check the deployment logs and ensure
  `app.py` and `requirements.txt` are present.
- **Font or emoji looks different:** appearance varies by device.

## Pre-launch checklist

- [ ] Add the real Instagram URL and contact email.
- [ ] Add an approved portrait or keep the placeholder.
- [ ] Review all website text and translations.
- [ ] Test the quiz and navigation on a phone.
- [ ] Review applicable privacy and business information requirements.
- [ ] Test any future email integration before claiming that messages
      are delivered.

