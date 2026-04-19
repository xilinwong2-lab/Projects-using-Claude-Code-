# Product Requirements Document
## AI Fashion App — Personal Style Assistant

**Version:** 1.0  
**Date:** April 2026  
**Status:** Draft

---

## 1. Overview

### 1.1 Problem Statement
Most people underuse their wardrobe. They struggle to put together outfits, forget what they own, and repeatedly buy items they don't need. Professional stylists are expensive and inaccessible to most people.

### 1.2 Solution
An AI-powered mobile app that digitizes the user's wardrobe, learns their personal style, and acts as a 24/7 personal stylist — suggesting outfits, recommending what to buy, and helping users look their best for any occasion.

### 1.3 Target Users
- Fashion-conscious individuals aged 18–40
- Frequent travellers who need context-aware outfit planning
- People wanting to make better use of clothes they already own
- Users who follow celebrity or influencer style

---

## 2. Goals & Success Metrics

| Goal | Metric | Target (6 months) |
|---|---|---|
| User engagement | Daily active users | 10,000 DAU |
| Core feature adoption | % users with 10+ items in closet | 60% |
| AI usage | AI outfit suggestions generated per week | 3 per active user |
| Retention | 30-day retention rate | 40% |
| Revenue | Monthly affiliate revenue | $5,000 |

---

## 3. Features

### 3.1 Digital Closet *(MVP)*

**Description:** Users photograph their clothing and the app automatically categorises, tags, and stores each item.

**User Stories:**
- As a user, I can take a photo of a clothing item so it is added to my closet.
- As a user, I can browse my closet filtered by category (tops, bottoms, dresses, etc.).
- As a user, I can manually edit an item's name, colour, or tags.
- As a user, I can mark items as favourites for quick access.
- As a user, I can delete items I no longer own.

**Acceptance Criteria:**
- Image upload completes in under 5 seconds on a standard 4G connection.
- Auto-classification correctly identifies category with ≥85% accuracy.
- Supports categories: top, bottom, dress, skirt, outerwear, accessory, shoes.
- Closet supports up to 500 items per user (free tier).

---

### 3.2 AI Outfit Suggestions *(MVP)*

**Description:** Claude AI analyses the user's wardrobe, style preferences, occasion, and destination to suggest outfit combinations.

**User Stories:**
- As a user, I can request outfit suggestions for a specific occasion (casual, formal, travel, beach).
- As a user, I can request suggestions for a travel destination and see outfits suited to that location's vibe.
- As a user, I can save AI-suggested outfits to my outfit library.
- As a user, I can rate suggestions (thumbs up/down) so the AI learns my taste.

**Acceptance Criteria:**
- AI returns 3 outfit suggestions per request.
- Each suggestion includes item IDs, a name, and a one-sentence styling tip.
- Response time under 8 seconds.
- Suggestions only use items from the user's own closet.

---

### 3.3 User Style Profile *(MVP)*

**Description:** Users complete a style profile covering body measurements, face shape, skin tone, and style preferences. This data personalises all AI outputs.

**User Stories:**
- As a user, I can enter my height, weight, body shape, and skin tone.
- As a user, I can select style keywords that describe my taste (e.g. minimalist, bohemian, streetwear).
- As a user, I can add celebrity or influencer names as style inspirations.
- As a user, I can update my profile at any time.

**Acceptance Criteria:**
- Profile setup takes under 3 minutes.
- All fields are optional — the app works with partial profiles.
- Style preferences are used in every AI outfit suggestion prompt.

---

### 3.4 Personalised Avatar & Virtual Try-On *(Phase 2)*

**Description:** Users create an avatar matching their body proportions to preview how outfits look before wearing them.

**User Stories:**
- As a user, I can create a 2D avatar by entering my measurements.
- As a user, I can overlay clothing items onto my avatar to preview outfits.
- As a user, I can share an outfit preview as an image.

**Acceptance Criteria:**
- Avatar supports height range 140cm–210cm and all body shapes.
- 2D overlay renders within 3 seconds.
- Exported image is at least 1080×1080px.

---

### 3.5 Facial & Body Shape Analysis *(Phase 2)*

**Description:** AI analyses an optional selfie to detect face shape and suggest flattering necklines, silhouettes, and colours.

**User Stories:**
- As a user, I can take or upload a selfie for face shape analysis.
- As a user, I receive style recommendations based on my detected face shape and body proportions.

**Acceptance Criteria:**
- Face shape detection returns one of: oval, round, square, heart, oblong.
- Recommendations map to at least 3 style attributes (neckline, silhouette, colour palette).
- Selfie is not stored permanently; processed and discarded after analysis.

---

### 3.6 Celebrity Style Integration *(Phase 2)*

**Description:** Users pick celebrities or influencers they admire. The AI maps those aesthetics to items the user already owns.

**User Stories:**
- As a user, I can search for and select celebrities as style references.
- As a user, I can request outfit suggestions inspired by a selected celebrity using my existing wardrobe.

**Acceptance Criteria:**
- Celebrity search returns results within 2 seconds.
- AI clearly labels suggestions as "inspired by [name]".
- Suggestions only use items in the user's wardrobe (no forced purchases).

---

### 3.7 Travel & Occasion Context *(Phase 2)*

**Description:** Users select a destination or event and preview their outfits against a matching background.

**User Stories:**
- As a user, I can enter a travel destination and get outfit suggestions suited to that location.
- As a user, I can preview my outfit against a 360° background image of the destination.

**Acceptance Criteria:**
- Background library contains at least 20 destination scenes at launch.
- Outfit suggestions include climate and cultural context in the styling note.

---

### 3.8 Shopping Recommendations *(Phase 2)*

**Description:** When the AI identifies a gap in the user's wardrobe, it recommends similar items from brand partners with affiliate links.

**User Stories:**
- As a user, I can request items to complete a specific look I don't fully own.
- As a user, I see brand recommendations with price, image, and a buy link.
- As a user, I can filter recommendations by price range.

**Acceptance Criteria:**
- At least one shopping API integrated (e.g. ASOS, Shopify partners).
- Affiliate links are clearly labelled.
- Results respect the user's preferred price range.

---

## 4. Technical Architecture

### 4.1 System Components

```
Mobile App (React Native)
        │
        ▼
API Layer (FastAPI / Python)
        │
   ┌────┴────┐
   │         │
SQLite/     AWS S3
PostgreSQL  (images)
        │
   ┌────┴─────────┐
   │              │
Claude API     Shopping API
(outfit AI,    (ASOS / Shopify)
 image vision)
```

### 4.2 API Endpoints (v1)

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Create account |
| POST | `/auth/login` | Login, return JWT |
| GET | `/auth/me` | Get current user profile |
| GET | `/closet/` | List closet items |
| POST | `/closet/` | Upload clothing item |
| DELETE | `/closet/{id}` | Remove item |
| PATCH | `/closet/{id}/favorite` | Toggle favourite |
| GET | `/outfits/` | List saved outfits |
| POST | `/outfits/` | Save a manual outfit |
| POST | `/outfits/ai-suggest` | Get AI outfit suggestions |
| DELETE | `/outfits/{id}` | Delete outfit |
| GET | `/shopping/recommendations` | Get brand recommendations |

### 4.3 Data Storage

| Data | Storage |
|---|---|
| User accounts & profiles | PostgreSQL |
| Clothing metadata | PostgreSQL |
| Outfit records | PostgreSQL |
| Clothing images | AWS S3 |
| Session tokens | JWT (stateless) |

---

## 5. Non-Functional Requirements

| Requirement | Target |
|---|---|
| API response time (p95) | < 500ms (excluding AI calls) |
| AI suggestion latency | < 8 seconds |
| Image upload size limit | 10MB per photo |
| Uptime | 99.5% monthly |
| Data encryption | TLS in transit, AES-256 at rest |
| GDPR compliance | Right to deletion, data export |
| Mobile platforms | iOS 15+ and Android 10+ |

---

## 6. Out of Scope (v1)

- Real-time video try-on
- Social sharing or community features
- Laundry tracking or outfit history logging
- Direct e-commerce checkout within the app
- Desktop/web version

---

## 7. Phased Rollout

### Phase 1 — MVP (Months 1–3)
- User auth (register / login)
- Digital closet (upload, auto-classify, browse)
- Style profile setup
- AI outfit suggestions (occasion + destination)

### Phase 2 — Growth (Months 4–6)
- 2D avatar and virtual try-on
- Facial and body shape analysis
- Celebrity style integration
- Travel context + destination backgrounds
- Shopping recommendations with affiliate links

### Phase 3 — Scale (Months 7–12)
- Outfit rating and AI learning loop
- Push notifications ("What to wear today?")
- Premium subscription tier
- Brand partnership programme

---

## 8. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| AI classification inaccuracy | Medium | Medium | Allow manual correction; use feedback to fine-tune prompts |
| Low closet upload rate | High | High | Onboarding nudges; batch upload flow |
| Shopping API unavailability | Low | Medium | Placeholder fallback; multiple API partners |
| User privacy concern over selfie analysis | Medium | High | On-device processing where possible; clear data policy; no permanent selfie storage |
| High Claude API costs at scale | Medium | High | Cache common suggestions; prompt caching; rate limits per user |

---

## 9. Open Questions

1. Should outfit history (what the user actually wore) be tracked? This could improve AI personalisation significantly.
2. Is a freemium model (limited AI suggestions per month) or subscription the right monetisation approach?
3. Which shopping API partner to integrate first — ASOS, Shopify, or a regional partner?
4. Should celebrity style matching use image search or a curated style database?
