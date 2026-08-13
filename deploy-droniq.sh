#!/usr/bin/env bash
# Deploy Droniq EN/IT landings + assets to the live nginx host.
# Usage:
#   export DEPLOY_HOST=your.server.com   # or IP
#   export DEPLOY_USER=youruser
#   export DEPLOY_PATH=/var/www/html      # or public_html
#   # optional: export DEPLOY_PORT=22
#   ./deploy-droniq.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
: "${DEPLOY_HOST:?Set DEPLOY_HOST}"
: "${DEPLOY_USER:?Set DEPLOY_USER}"
: "${DEPLOY_PATH:?Set DEPLOY_PATH (e.g. /var/www/html or public_html)}"
PORT="${DEPLOY_PORT:-22}"

REMOTE="${DEPLOY_USER}@${DEPLOY_HOST}"
SSH=(ssh -p "$PORT" -o StrictHostKeyChecking=accept-new)
RSYNC=(rsync -avz --progress -e "ssh -p $PORT -o StrictHostKeyChecking=accept-new")

echo "→ Creating remote dirs on $REMOTE:$DEPLOY_PATH"
"${SSH[@]}" "$REMOTE" "mkdir -p \
  '$DEPLOY_PATH/en/droniq' \
  '$DEPLOY_PATH/it/droniq' \
  '$DEPLOY_PATH/assets/css' \
  '$DEPLOY_PATH/assets/js' \
  '$DEPLOY_PATH/assets/img/products/droniq' \
  '$DEPLOY_PATH/assets/img/reviews/droniq'"

echo "→ Syncing EN/IT pages"
"${RSYNC[@]}" "$ROOT/en/droniq/" "$REMOTE:$DEPLOY_PATH/en/droniq/"
"${RSYNC[@]}" "$ROOT/it/droniq/" "$REMOTE:$DEPLOY_PATH/it/droniq/"

echo "→ Syncing CSS/JS"
"${RSYNC[@]}" "$ROOT/assets/css/droniq-landing.css" "$REMOTE:$DEPLOY_PATH/assets/css/"
"${RSYNC[@]}" "$ROOT/assets/js/droniq-landing.js" "$REMOTE:$DEPLOY_PATH/assets/js/"

echo "→ Syncing images/video"
"${RSYNC[@]}" "$ROOT/assets/img/products/droniq/" "$REMOTE:$DEPLOY_PATH/assets/img/products/droniq/"
"${RSYNC[@]}" "$ROOT/assets/img/reviews/droniq/" "$REMOTE:$DEPLOY_PATH/assets/img/reviews/droniq/"

echo "→ Syncing sitemap"
"${RSYNC[@]}" "$ROOT/sitemap.xml" "$REMOTE:$DEPLOY_PATH/sitemap.xml"

echo "✓ Deploy done. Check:"
echo "  https://spotspectrum.com/en/droniq/landing.html"
echo "  https://spotspectrum.com/it/droniq/landing.html"
