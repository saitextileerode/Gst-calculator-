# GST Calculator (Android)

Amount + GST (Plus) and Amount - GST (Minus) calculator with CGST / SGST breakdown.
Built with Capacitor. The APK is built online by GitHub Actions.

## Quick steps
1. Create a new GitHub repository.
2. Upload ALL files from this folder (including the hidden `.github` folder).
3. Open the **Actions** tab -> **Build GST Calculator APK** -> **Run workflow**.
4. After about 5-8 minutes open the finished run (green tick):
   - **Releases** (right side of the repo page) -> download `GST-Calculator.apk`, or
   - **Artifacts** at the bottom of the run -> `GST-Calculator-APK`.
5. Open the APK on the phone and install it (allow "Install unknown apps" when asked).

## Change things later
- Screen and logic: `www/index.html`
- Default rates: `var DEFAULTS = [3, 5, 12, 18, 40];` in `www/index.html`
- App name / id: `capacitor.config.json`
