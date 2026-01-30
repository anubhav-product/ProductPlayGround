# Quick Reference: New Features

## Learning Resources Tab

### Access
`/app?tab=resources`

### Content
- **PM Fundamentals** (3 playlists)
- **AI Product Management** (3 playlists)  
- **Product Analytics** (3 playlists)

### Key Points
- Static content (no tracking)
- External YouTube links
- Complements judgment, doesn't replace it

---

## Walkthrough Mode

### How to Use

1. **Enable**: Check "🧭 Enable Walkthrough Mode" in Challenge tab
2. **Step 1**: Answer problem framing questions
3. **Step 2**: Form your hypotheses
4. **Step 3**: AI builds on YOUR thinking
5. **Step 4**: Review tradeoffs and risks
6. **Step 5**: Get next steps, download analysis

### Exit Anytime
Uncheck the walkthrough mode toggle to return to regular analysis

### AI Language Style
- ✅ "One possible approach is..."
- ✅ "A risk to consider is..."
- ❌ "The best choice is..."
- ❌ Numerical scores

---

## Files Modified

### Frontend
- `templates/index.html` - Added walkthrough UI and resources tab

### Backend
- `flask_app.py` - Added `/analyze-walkthrough` route
- `app/prompt.py` - Added walkthrough analysis methods

### Documentation
- `docs/NEW-FEATURES.md` - Comprehensive feature documentation
- `docs/QUICK-REFERENCE.md` - This file

---

## URL Patterns

| Feature | URL |
|---------|-----|
| Challenge (Regular) | `/app?tab=challenge` |
| Challenge (Walkthrough) | `/app?tab=challenge` + toggle ON |
| KPI Dashboard | `/app?tab=kpi` |
| Product Teardown | `/app?tab=teardown` |
| Learning Resources | `/app?tab=resources` |

---

## Testing Checklist

- [ ] Learning Resources tab loads
- [ ] All 9 resource cards display
- [ ] External links open in new tabs
- [ ] Walkthrough Mode toggle works
- [ ] All 5 steps navigate correctly
- [ ] Step indicators update
- [ ] AI analysis returns successfully
- [ ] PDF download works in walkthrough
- [ ] Can exit walkthrough anytime
- [ ] Visual consistency maintained

---

## Key Product Principles (Maintained)

1. ✅ No automation of decisions
2. ✅ No scoring or ranking
3. ✅ AI guides thinking, not prescribes
4. ✅ Decision ownership stays with user
5. ✅ Emphasis on tradeoffs and uncertainty
6. ✅ Learning-focused approach

---

## Support

For issues or questions:
1. Check `docs/NEW-FEATURES.md` for detailed documentation
2. Review Flask server logs for backend errors
3. Check browser console for frontend errors
4. Verify OpenAI API key is configured in `.env`
