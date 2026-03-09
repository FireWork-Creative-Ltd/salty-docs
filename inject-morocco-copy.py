#!/usr/bin/env python3
"""
Inject fresh, humanized Meta ad copy into all Morocco execution tab fields.
Applies SALTY brand voice + VIKING word principles + hook variation strategy.

Audience tailoring:
  NA = aspiration ("what if your life looked different?")
  EU = proximity/value ("3 hours from London, from EUR 1,950")
  LLA Purchases = social proof ("hundreds booked, zero regrets")
  LLA Website = social proof ("you looked, they booked")
  Surf Community = tribe identity ("your people, your waves")

Run: python3 salty-docs/inject-morocco-copy.py
"""

import re
import os

# ─────────────────────────────────────────────
# ALL MOROCCO COPY — 405 fields
# Key format: em-{t|r|m|b}-{adset}-{creative#}-{p|h|c}{1|2|3}
# ─────────────────────────────────────────────

copy = {}

# ═══════════════════════════════════════════════
# TOF — NORTH AMERICA (aspiration angle)
# ═══════════════════════════════════════════════

# Creative #1: Brett 'Feel Like Sh**' (Video / 8s)
copy["em-t-na-1-p1"] = "You ever just feel like absolute sh**? Yeah. Us too. So we built a trip for that exact feeling. Morocco. May 16&ndash;23. Surf at sunrise. Rooftop yoga. Friends you haven&rsquo;t made yet. SALTY Retreats."
copy["em-t-na-1-p2"] = "Monday morning. Same alarm. Same commute. Same everything. What if next Monday you woke up in Morocco instead? Sand under your feet. Salt in your hair. 20 people who feel like family by dinner. SALTY Retreats. May 16&ndash;23."
copy["em-t-na-1-p3"] = "What if the best week of your year started with a ticket to Morocco? 7 nights. Surf. Yoga. Food that ruins every restaurant back home. A crew of strangers who won&rsquo;t feel like strangers. SALTY Retreats. May 16&ndash;23."
copy["em-t-na-1-h1"] = "Feel Like Sh**? Same. Let&rsquo;s Go."
copy["em-t-na-1-h2"] = "Trade Your Couch for Morocco"
copy["em-t-na-1-h3"] = "Your Sign to Book the Trip"
copy["em-t-na-1-c1"] = "Watch More"
copy["em-t-na-1-c2"] = "Learn More"
copy["em-t-na-1-c3"] = "Sign Up"

# Creative #2: 9-5 Erin NA (Video / 15-20s)
copy["em-t-na-2-p1"] = "I used to think burning out meant I was working hard enough. Then I booked a trip to Morocco and remembered what it feels like to actually want to get out of bed. Surf at dawn. Train hard. Eat food that changes you. Come home different. SALTY Retreats. May 16&ndash;23."
copy["em-t-na-2-p2"] = "You don&rsquo;t need to earn a vacation. You need to take one. 7 nights in Morocco: surf coaching every morning, yoga at sunset, dinners where nobody checks their phone, and a crew who gets it. SALTY Retreats. May 16&ndash;23. All-inclusive. All levels."
copy["em-t-na-2-p3"] = "Sunday scaries. Monday dread. Tuesday counting down to Friday. Sound familiar? Now picture this: waking up in Morocco. Surfing before breakfast. Yoga overlooking the Atlantic. Laughing until your face hurts. That&rsquo;s a SALTY week. May 16&ndash;23."
copy["em-t-na-2-h1"] = "The 9-5 Can Wait"
copy["em-t-na-2-h2"] = "Remember What Living Feels Like"
copy["em-t-na-2-h3"] = "You Deserve More Than a Weekend"
copy["em-t-na-2-c1"] = "Watch More"
copy["em-t-na-2-c2"] = "Learn More"
copy["em-t-na-2-c3"] = "Sign Up"

# Creative #4: So Much Fun Workout (Video / 15-30s)
copy["em-t-na-4-p1"] = "Beach sprints. Partner carries. Rooftop yoga. Dancing that somehow counts as cardio. This is fitness when you strip away the screens and the fluorescent lights and just move because it feels good. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-t-na-4-p2"] = "When was the last time you finished a workout and actually smiled? Not because you hit a PR. Because it was genuinely fun. That&rsquo;s every single day at SALTY. Beach training. Surf coaching. Yoga with ocean views. Morocco. May 16&ndash;23."
copy["em-t-na-4-p3"] = "Your gym has AC. We have the Atlantic Ocean. Your gym has mirrors. We have sunrises. Your gym has a playlist. We have live drums and 20 people losing their minds. SALTY Retreats. Morocco. May 16&ndash;23. Make fun of wellness."
copy["em-t-na-4-h1"] = "Workouts That Don&rsquo;t Suck"
copy["em-t-na-4-h2"] = "Ditch the Gym. Hit the Beach."
copy["em-t-na-4-h3"] = "Fitness Meets Adventure"
copy["em-t-na-4-c1"] = "Watch More"
copy["em-t-na-4-c2"] = "Learn More"
copy["em-t-na-4-c3"] = "Sign Up"

# Creative #5: Sarah Partnership (Video / 30-60s)
copy["em-t-na-5-p1"] = "Sarah&rsquo;s going to Morocco with SALTY this May. Hear why she can&rsquo;t stop talking about it &mdash; surf, food, community, and a week that&rsquo;s nothing like a typical trip. May 16&ndash;23. Limited spots."
copy["em-t-na-5-p2"] = "There&rsquo;s a reason Sarah said yes to this trip in under 24 hours. Morocco. Surf coaching. Rooftop dinners. 20 people who show up as strangers and leave as friends. Watch her explain it better than we can. SALTY Retreats. May 16&ndash;23."
copy["em-t-na-5-p3"] = "When Sarah tells you a trip changed how she thinks about travel, you listen. Morocco with SALTY. May 16&ndash;23. Surf. Yoga. Food. Community. All-inclusive. Limited to 20 guests."
copy["em-t-na-5-h1"] = "Why She Chose Morocco"
copy["em-t-na-5-h2"] = "This Trip Changes People"
copy["em-t-na-5-h3"] = "Not Your Average Holiday"
copy["em-t-na-5-c1"] = "Watch More"
copy["em-t-na-5-c2"] = "Learn More"
copy["em-t-na-5-c3"] = "Sign Up"

# Creative #6: Girls Solo Travel (Video / 15-30s)
copy["em-t-na-6-p1"] = "67% of SALTY guests book solo. Most of them are women. Not because they don&rsquo;t have friends &mdash; because this is the kind of trip that&rsquo;s better when you show up open. By dinner on night one, you&rsquo;ll have a crew. Morocco. May 16&ndash;23."
copy["em-t-na-6-p2"] = "You don&rsquo;t need a travel buddy. You don&rsquo;t need to \"be brave.\" You just need to book. 67% of our guests come alone. Every single one leaves with 19 new friends. SALTY Retreats. Morocco. May 16&ndash;23. All-inclusive. All levels."
copy["em-t-na-6-p3"] = "She showed up in Morocco knowing nobody. By day two, she had dinner plans with the whole group. By day five, they were planning their next trip together. That&rsquo;s what happens at SALTY. You arrive solo. You leave with a crew. May 16&ndash;23."
copy["em-t-na-6-h1"] = "67% Book Solo. 0% Stay Alone."
copy["em-t-na-6-h2"] = "Solo Trip. Instant Crew."
copy["em-t-na-6-h3"] = "Your People Are Waiting"
copy["em-t-na-6-c1"] = "Watch More"
copy["em-t-na-6-c2"] = "Learn More"
copy["em-t-na-6-c3"] = "Sign Up"

# Creative #7: Are Retreats for Men? (Video / 30-60s)
copy["em-t-na-7-p1"] = "\"Wellness retreat\" sounds like something your girlfriend drags you to. Here&rsquo;s what it actually is at SALTY: surf every morning. Hard training sessions. Moroccan food that&rsquo;ll wreck every restaurant back home. And 20 people who just want a damn good week. No crystals. No sound baths. May 16&ndash;23."
copy["em-t-na-7-p2"] = "Name one thing wrong with surfing every morning, eating incredible food, training with people who push you, and spending a week in Morocco with strangers who become your best mates. Exactly. SALTY Retreats. May 16&ndash;23. Yes, it&rsquo;s for you."
copy["em-t-na-7-p3"] = "I&rsquo;ll be honest &mdash; I rolled my eyes at \"wellness retreat\" too. Then I actually went. Turns out it&rsquo;s just fitness, adventure, great food, and incredible people in a place you&rsquo;d never go alone. No gongs. No juice cleanses. Just the best week of your year. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-t-na-7-h1"] = "This Isn&rsquo;t Your Girlfriend&rsquo;s Retreat"
copy["em-t-na-7-h2"] = "Surf. Train. Eat. Repeat."
copy["em-t-na-7-h3"] = "Guys, This One&rsquo;s for You"
copy["em-t-na-7-c1"] = "Watch More"
copy["em-t-na-7-c2"] = "Learn More"
copy["em-t-na-7-c3"] = "Sign Up"

# ═══════════════════════════════════════════════
# TOF — EUROPE (proximity/value angle)
# ═══════════════════════════════════════════════

# Creative #1: Brett 'Feel Like Sh**' (EU)
copy["em-t-eu-1-p1"] = "You ever just feel like absolute sh**? Morocco is 3 hours from London. No jet lag. A completely different world. Surf. Yoga. Food that&rsquo;ll ruin you. 7 nights, all-inclusive, from &pound;1,700. SALTY Retreats. May 16&ndash;23."
copy["em-t-eu-1-p2"] = "Same grey sky. Same routine. Same walls. What if you swapped all of it for a week on the Moroccan coast? Surf at dawn. Rooftop yoga. A crew that feels like home by day two. 3 hours from London. From EUR 1,950. SALTY Retreats. May 16&ndash;23."
copy["em-t-eu-1-p3"] = "For less than a week in Spain, you get 7 nights in Morocco with surf coaching, yoga, all meals, excursions, and 20 people who&rsquo;ll become your new mates. 3 hours from London. Direct flights under &pound;80. SALTY Retreats. May 16&ndash;23."
copy["em-t-eu-1-h1"] = "3 Hours Away. A World Apart."
copy["em-t-eu-1-h2"] = "Swap the Grey for Morocco"
copy["em-t-eu-1-h3"] = "Closer Than You Think"
copy["em-t-eu-1-c1"] = "Watch More"
copy["em-t-eu-1-c2"] = "Learn More"
copy["em-t-eu-1-c3"] = "Sign Up"

# Creative #3: 9-5 Erin EU (Video / 15-20s)
copy["em-t-eu-3-p1"] = "I wanted more from my holidays than a sunbed and a buffet. So I tried something different: a week in Morocco with people who believe fun is part of feeling good. Surf coaching every morning. Rooftop yoga. Food you&rsquo;ll dream about. SALTY Retreats. May 16&ndash;23. From EUR 1,950."
copy["em-t-eu-3-p2"] = "There&rsquo;s a version of travel where you come back better than you left. Not \"self-improvement\" better. Just &mdash; alive. 7 nights in Morocco. Surf. Yoga. Food. Community. 3 hours from London. From GBP 1,700. SALTY Retreats. May 16&ndash;23."
copy["em-t-eu-3-p3"] = "Most holidays are fine. Forgettable, but fine. This one&rsquo;s different. 7 nights in a Moroccan surf town with coaching, yoga, incredible food, and 20 people who make it the kind of trip you talk about for years. From EUR 1,950. Everything included. SALTY Retreats. May 16&ndash;23."
copy["em-t-eu-3-h1"] = "More Than a Holiday"
copy["em-t-eu-3-h2"] = "Travel That Changes You"
copy["em-t-eu-3-h3"] = "The Trip You&rsquo;ll Talk About"
copy["em-t-eu-3-c1"] = "Watch More"
copy["em-t-eu-3-c2"] = "Learn More"
copy["em-t-eu-3-c3"] = "Sign Up"

# Creative #4: So Much Fun Workout (EU)
copy["em-t-eu-4-p1"] = "This is what happens when workouts are actually fun. Beach sprints. Partner carries. Rooftop yoga. Dancing that somehow counts as cardio. No bootcamp energy. No bland hotel gym. Just 7 days where your body thanks you. SALTY Retreats. Morocco. May 16&ndash;23. From EUR 1,950."
copy["em-t-eu-4-p2"] = "Your gym: mirrors, machines, the same playlist for 3 months. SALTY Morocco: the Atlantic Ocean, sunrise surf, rooftop yoga, and training on the beach with 20 people who actually want to be there. 3 hours from London. May 16&ndash;23. From GBP 1,700."
copy["em-t-eu-4-p3"] = "Come for the surf. Stay for the dance sessions. Leave with muscles you forgot you had and stories your gym friends won&rsquo;t believe. 7 nights in Morocco. Everything included. All fitness levels. SALTY Retreats. May 16&ndash;23."
copy["em-t-eu-4-h1"] = "Your Gym Could Never"
copy["em-t-eu-4-h2"] = "Fitness Meets the Atlantic"
copy["em-t-eu-4-h3"] = "Train. Surf. Dance. Repeat."
copy["em-t-eu-4-c1"] = "Watch More"
copy["em-t-eu-4-c2"] = "Learn More"
copy["em-t-eu-4-c3"] = "Sign Up"

# Creative #5: Sarah Partnership (EU)
copy["em-t-eu-5-p1"] = "Sarah&rsquo;s heading to Morocco with SALTY this May &mdash; and she hasn&rsquo;t stopped talking about it. Surf, food, community, and a week that doesn&rsquo;t feel like a typical holiday. 3 hours from London. From GBP 1,700. All-inclusive. May 16&ndash;23."
copy["em-t-eu-5-p2"] = "When someone you trust says \"this trip is different,\" it means something. Sarah chose SALTY Morocco and here&rsquo;s why. Surf coaching. Rooftop dinners. 20 people. 7 nights. Everything included. Direct flights under &pound;80. May 16&ndash;23."
copy["em-t-eu-5-p3"] = "Sarah booked in 24 hours. Her spot is taken. Yours might not be. Morocco with SALTY. May 16&ndash;23. Surf. Yoga. Food. Community. From EUR 1,950 all-inclusive. 3 hours from London."
copy["em-t-eu-5-h1"] = "Why She Chose Morocco"
copy["em-t-eu-5-h2"] = "This Trip Is Different"
copy["em-t-eu-5-h3"] = "See What She&rsquo;s Excited About"
copy["em-t-eu-5-c1"] = "Watch More"
copy["em-t-eu-5-c2"] = "Learn More"
copy["em-t-eu-5-c3"] = "Sign Up"

# Creative #6: Girls Solo Travel (EU)
copy["em-t-eu-6-p1"] = "67% of our guests book solo. Most of them are women. Not because they&rsquo;re lonely &mdash; because this is the kind of trip where strangers become your people by day two. You don&rsquo;t need a travel partner. SALTY Retreats. Morocco. May 16&ndash;23. From EUR 1,950. 3 hours from London."
copy["em-t-eu-6-p2"] = "Thinking about going but don&rsquo;t have anyone to go with? Good. You&rsquo;ll meet 19 other people who felt the same way. By dinner on night one, you&rsquo;ll wonder why you ever waited. SALTY Retreats. Morocco. May 16&ndash;23. All-inclusive from GBP 1,700."
copy["em-t-eu-6-p3"] = "\"I almost didn&rsquo;t come because I was nervous about going alone. Best decision I ever made.\" &mdash; That&rsquo;s what we hear every single retreat. SALTY Morocco. May 16&ndash;23. Solo-friendly. All-inclusive. 3 hours from London."
copy["em-t-eu-6-h1"] = "Solo Trip. Instant Friends."
copy["em-t-eu-6-h2"] = "You Don&rsquo;t Need a Plus-One"
copy["em-t-eu-6-h3"] = "67% Come Solo. All Leave Happy."
copy["em-t-eu-6-c1"] = "Watch More"
copy["em-t-eu-6-c2"] = "Learn More"
copy["em-t-eu-6-c3"] = "Sign Up"

# Creative #7: Are Retreats for Men? (EU)
copy["em-t-eu-7-p1"] = "If someone said \"wellness retreat\" to me five years ago, I&rsquo;d have pictured smoothie bowls and silence. Here&rsquo;s what it actually is: surf coaching every morning. Real training. Moroccan food that&rsquo;ll ruin every restaurant back home. 20 people having the week of their lives. SALTY Retreats. Morocco. May 16&ndash;23. From EUR 1,950."
copy["em-t-eu-7-p2"] = "No gongs. No juice cleanses. No one asking you to journal about your feelings. Just surf, hard training, incredible food, and the best people you&rsquo;ll meet all year. SALTY Retreats. Morocco. May 16&ndash;23. 3 hours from London. From GBP 1,700. All-inclusive."
copy["em-t-eu-7-p3"] = "Your mates go to Ibiza. You could do better. 7 nights in Morocco: surf every morning, proper training sessions, food you&rsquo;ll be talking about for months, and 20 people who aren&rsquo;t trying to impress anyone. SALTY Retreats. May 16&ndash;23. From EUR 1,950."
copy["em-t-eu-7-h1"] = "Not What You Think"
copy["em-t-eu-7-h2"] = "No Gongs. Just Good Times."
copy["em-t-eu-7-h3"] = "Surf. Train. Eat. Repeat."
copy["em-t-eu-7-c1"] = "Watch More"
copy["em-t-eu-7-c2"] = "Learn More"
copy["em-t-eu-7-c3"] = "Sign Up"

# Creative #8: 3 Hours From London (EU only)
copy["em-t-eu-8-p1"] = "Morocco is closer than your nan&rsquo;s house. 3 hours from London. 2.5 from Paris. Direct flights under &pound;80. 7 nights of surf, yoga, ridiculous food, and a crew that feels like home. SALTY Retreats. May 16&ndash;23. From GBP 1,700. Everything included."
copy["em-t-eu-8-p2"] = "You&rsquo;d spend more on a rainy week in Cornwall. Morocco: 3 hours from London. Direct flights from &pound;50. 7 nights all-inclusive from GBP 1,700. Surf coaching. Yoga. All meals. Excursions. A tan. SALTY Retreats. May 16&ndash;23."
copy["em-t-eu-8-p3"] = "London to Morocco: 3 hours. Flight cost: under &pound;80. Trip cost: from GBP 1,700 all-inclusive. What you get: 7 nights, surf coaching, yoga, all meals, excursions, transfers, and 20 new friends. SALTY Retreats. May 16&ndash;23."
copy["em-t-eu-8-h1"] = "3 Hours. No Jet Lag. New Life."
copy["em-t-eu-8-h2"] = "Closer Than Cornwall"
copy["em-t-eu-8-h3"] = "Your Best Trip Costs Less"
copy["em-t-eu-8-c1"] = "Learn More"
copy["em-t-eu-8-c2"] = "Watch More"
copy["em-t-eu-8-c3"] = "Sign Up"

# ═══════════════════════════════════════════════
# TOF — LLA PURCHASES (social proof angle)
# ═══════════════════════════════════════════════

# Creative #1: Brett (LLA Purchases)
copy["em-t-lp-1-p1"] = "Hundreds of people have taken this trip. Zero have regretted it. You ever feel like sh**? Here&rsquo;s the fix: Morocco. May 16&ndash;23. Surf. Yoga. A crew of 20 who&rsquo;ll feel like home. SALTY Retreats."
copy["em-t-lp-1-p2"] = "7 retreats. Hundreds of guests. A waitlist that fills up faster each time. And it started with the same feeling you have right now: \"I need to get the hell out of here.\" SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-t-lp-1-p3"] = "Our last three retreats sold out in weeks. Morocco is next. May 16&ndash;23. Surf at dawn. Yoga at sunset. Dinner with people who feel like old friends. SALTY Retreats. Limited to 20 spots."
copy["em-t-lp-1-h1"] = "Hundreds Booked. Zero Regrets."
copy["em-t-lp-1-h2"] = "The Trip Everyone&rsquo;s Talking About"
copy["em-t-lp-1-h3"] = "Spots Fill Fast. Just Saying."
copy["em-t-lp-1-c1"] = "Watch More"
copy["em-t-lp-1-c2"] = "Learn More"
copy["em-t-lp-1-c3"] = "Sign Up"

# Creative #4: So Much Fun Workout (LLA Purchases)
copy["em-t-lp-4-p1"] = "Our past guests won&rsquo;t shut up about the workouts. Beach sprints at sunrise. Rooftop yoga with ocean views. Training that makes you laugh as much as it makes you sweat. Join them. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-t-lp-4-p2"] = "\"I haven&rsquo;t felt this good in years.\" That&rsquo;s what guests tell us after a week of SALTY training. Beach workouts. Surf coaching. Yoga. All of it fun. None of it boring. Morocco. May 16&ndash;23."
copy["em-t-lp-4-p3"] = "40% of our guests come back for a second trip. The workouts are a big reason why. Beach sprints. Partner carries. Yoga on rooftops. All levels. All fun. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-t-lp-4-h1"] = "They Came Back for More"
copy["em-t-lp-4-h2"] = "Workouts That Keep You Coming"
copy["em-t-lp-4-h3"] = "Join 300+ Past Guests"
copy["em-t-lp-4-c1"] = "Watch More"
copy["em-t-lp-4-c2"] = "Learn More"
copy["em-t-lp-4-c3"] = "Sign Up"

# Creative #6: Girls Solo Travel (LLA Purchases)
copy["em-t-lp-6-p1"] = "67% of SALTY guests book solo. Most are women. They keep coming back. This time it&rsquo;s Morocco &mdash; surf, yoga, rooftop dinners, and 19 strangers who become your people. May 16&ndash;23. All-inclusive."
copy["em-t-lp-6-p2"] = "The guests who book solo are the ones who come back. And bring friends. And text us for months after. That&rsquo;s SALTY. Morocco. May 16&ndash;23. Limited to 20. All-inclusive."
copy["em-t-lp-6-p3"] = "Hundreds of solo travelers. Not a single one who wished they&rsquo;d stayed home. Morocco is next. May 16&ndash;23. Surf. Yoga. Food. Friends. All-inclusive. SALTY Retreats."
copy["em-t-lp-6-h1"] = "Hundreds Came Solo. All Left Happy."
copy["em-t-lp-6-h2"] = "The Solo Trip That Sells Itself"
copy["em-t-lp-6-h3"] = "67% Solo. 100% Worth It."
copy["em-t-lp-6-c1"] = "Watch More"
copy["em-t-lp-6-c2"] = "Learn More"
copy["em-t-lp-6-c3"] = "Sign Up"

# ═══════════════════════════════════════════════
# TOF — LLA WEBSITE (social proof angle)
# ═══════════════════════════════════════════════

# Creative #1: Brett (LLA Website)
copy["em-t-lw-1-p1"] = "Everyone&rsquo;s tired of feeling like sh**. Some people actually do something about it. They book Morocco. Surf at dawn. Yoga at sunset. A crew that hits different. May 16&ndash;23. SALTY Retreats."
copy["em-t-lw-1-p2"] = "You looked. They booked. And every single one of them says the same thing: \"Why didn&rsquo;t I do this sooner?\" Morocco. May 16&ndash;23. Surf. Yoga. 20 incredible people. All-inclusive. SALTY Retreats."
copy["em-t-lw-1-p3"] = "You&rsquo;ve been thinking about it. We know because people just like you already took the leap. Morocco. May 16&ndash;23. 7 nights. Surf. Yoga. Food. Community. SALTY Retreats."
copy["em-t-lw-1-h1"] = "They Went. You&rsquo;re Next."
copy["em-t-lw-1-h2"] = "Stop Thinking. Start Packing."
copy["em-t-lw-1-h3"] = "People Like You Loved This"
copy["em-t-lw-1-c1"] = "Watch More"
copy["em-t-lw-1-c2"] = "Learn More"
copy["em-t-lw-1-c3"] = "Sign Up"

# Creative #2: 9-5 Erin NA (LLA Website)
copy["em-t-lw-2-p1"] = "The 9-5 had her running on empty. Morocco brought her back to life. Surf at dawn. Real food. Real people. A week where \"what do you do?\" is the last question anyone asks. SALTY Retreats. May 16&ndash;23."
copy["em-t-lw-2-p2"] = "She used to think vacations meant recovering from work. Then she tried SALTY Morocco and realized vacation should make you feel alive, not just rested. Surf. Yoga. 20 people who get it. May 16&ndash;23."
copy["em-t-lw-2-p3"] = "Burning out in style isn&rsquo;t a personality. But booking a week in Morocco? That&rsquo;s a power move. Surf coaching. Rooftop yoga. Meals that change you. SALTY Retreats. May 16&ndash;23. All-inclusive."
copy["em-t-lw-2-h1"] = "She Quit Burning Out"
copy["em-t-lw-2-h2"] = "What She Did Instead"
copy["em-t-lw-2-h3"] = "Trade the Grind for Morocco"
copy["em-t-lw-2-c1"] = "Watch More"
copy["em-t-lw-2-c2"] = "Learn More"
copy["em-t-lw-2-c3"] = "Sign Up"

# Creative #4: So Much Fun Workout (LLA Website)
copy["em-t-lw-4-p1"] = "They said \"best workouts of my life.\" Not because they were the hardest. Because they were on the beach. In the ocean. On rooftops. With people who laugh harder than they lunge. SALTY Morocco. May 16&ndash;23."
copy["em-t-lw-4-p2"] = "Past guests keep asking when they can come back. Something about beach sprints at sunrise, yoga with the Atlantic behind you, and training that doesn&rsquo;t feel like training. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-t-lw-4-p3"] = "Your gym&rsquo;s got nothing on the Moroccan coast. Surf coaching. Beach fitness. Rooftop yoga. Dancing. All of it included. All levels welcome. SALTY Retreats. May 16&ndash;23."
copy["em-t-lw-4-h1"] = "Best Workouts of Their Lives"
copy["em-t-lw-4-h2"] = "Past Guests Keep Coming Back"
copy["em-t-lw-4-h3"] = "Better Than Your Gym"
copy["em-t-lw-4-c1"] = "Watch More"
copy["em-t-lw-4-c2"] = "Learn More"
copy["em-t-lw-4-c3"] = "Sign Up"

# ═══════════════════════════════════════════════
# TOF — SURF COMMUNITY (tribe identity angle)
# ═══════════════════════════════════════════════

# Creative #1: Brett (Surf Community)
copy["em-t-sc-1-p1"] = "You know that feeling when the swell is up and you&rsquo;ve got nowhere to be? That&rsquo;s every morning in Morocco. May 16&ndash;23. Daily surf coaching in Taghazout. Plus yoga, training, and a crew of 20 who live for it. SALTY Retreats."
copy["em-t-sc-1-p2"] = "Taghazout. Seven days. Endless right-handers. Coaching for every level from first-timer to shortboard. Add rooftop yoga, Moroccan food, and a crew that speaks your language. SALTY Retreats. May 16&ndash;23."
copy["em-t-sc-1-p3"] = "Dawn patrol in Morocco hits different. Empty lineups. Warm water. Coaches who&rsquo;ll actually make you better. The rest of the day? Yoga, beach training, food that&rsquo;ll ruin you. SALTY Retreats. May 16&ndash;23."
copy["em-t-sc-1-h1"] = "Surf Morocco. 7 Days. All In."
copy["em-t-sc-1-h2"] = "Your Next Dawn Patrol"
copy["em-t-sc-1-h3"] = "Taghazout Is Calling"
copy["em-t-sc-1-c1"] = "Watch More"
copy["em-t-sc-1-c2"] = "Learn More"
copy["em-t-sc-1-c3"] = "Sign Up"

# Creative #4: So Much Fun Workout (Surf Community)
copy["em-t-sc-4-p1"] = "Surf needs more than paddle strength. Beach sprints for speed. Yoga for flexibility. Partner carries for power. We built the training around what makes you a better surfer. SALTY Morocco. May 16&ndash;23."
copy["em-t-sc-4-p2"] = "Surf every morning. Train hard every afternoon. Yoga to keep everything loose. Then dinner on the roof watching the sun drop into the Atlantic. That&rsquo;s a SALTY week in Morocco. May 16&ndash;23."
copy["em-t-sc-4-p3"] = "You came for the surf. You&rsquo;ll stay for the training. Beach workouts, partner drills, rooftop yoga &mdash; everything designed to complement your time in the water. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-t-sc-4-h1"] = "Surf Better. Train Smarter."
copy["em-t-sc-4-h2"] = "Built for Surfers"
copy["em-t-sc-4-h3"] = "Beyond the Break"
copy["em-t-sc-4-c1"] = "Watch More"
copy["em-t-sc-4-c2"] = "Learn More"
copy["em-t-sc-4-c3"] = "Sign Up"

# Creative #5: Sarah Partnership (Surf Community)
copy["em-t-sc-5-p1"] = "Sarah&rsquo;s headed to Taghazout with SALTY for surf, yoga, and a week with 20 people who live for the ocean. Hear why she&rsquo;s more excited about this than any trip she&rsquo;s taken. Morocco. May 16&ndash;23."
copy["em-t-sc-5-p2"] = "When a surfer picks a trip, they don&rsquo;t pick random. Sarah chose SALTY Morocco for the coaching, the waves, and the kind of crew you only find when everyone shares the same stoke. May 16&ndash;23."
copy["em-t-sc-5-p3"] = "Taghazout. Legendary right-handers. Daily coaching. Sarah&rsquo;s in. Are you? SALTY Retreats. Morocco. May 16&ndash;23. Surf. Yoga. Community. All-inclusive. Limited spots."
copy["em-t-sc-5-h1"] = "Why She Chose Taghazout"
copy["em-t-sc-5-h2"] = "A Surfer&rsquo;s Kind of Trip"
copy["em-t-sc-5-h3"] = "The Lineup&rsquo;s Filling Up"
copy["em-t-sc-5-c1"] = "Watch More"
copy["em-t-sc-5-c2"] = "Learn More"
copy["em-t-sc-5-c3"] = "Sign Up"

# ═══════════════════════════════════════════════
# RE-ENGAGEMENT (warm, permissive, "door's still open")
# ═══════════════════════════════════════════════

# Creative #9: 'It Might Be Time' Carousel
copy["em-r-ps-9-p1"] = "You&rsquo;ve been thinking about it. We know because you looked at Panama. Maybe Sri Lanka. Something didn&rsquo;t line up. That&rsquo;s fine. Morocco is next &mdash; and honestly, it might be the one. 7 nights. Surf. Yoga. All-inclusive. May 16&ndash;23. The door&rsquo;s open."
copy["em-r-ps-9-p2"] = "Last time, the timing wasn&rsquo;t right. Or the budget. Or maybe you just weren&rsquo;t ready. No judgment. But Morocco is happening May 16&ndash;23, and we saved you a spot. Surf. Food. Community. All-inclusive. Message us when you&rsquo;re ready."
copy["em-r-ps-9-p3"] = "You almost booked before. And we bet you still think about it. Morocco is next &mdash; May 16&ndash;23. Closer, incredible, and spots are going faster than Panama or Sri Lanka. No pressure. Just answers. Message us."
copy["em-r-ps-9-h1"] = "It Might Be Time"
copy["em-r-ps-9-h2"] = "The Door&rsquo;s Still Open"
copy["em-r-ps-9-h3"] = "Ready When You Are"
copy["em-r-ps-9-c1"] = "See Trip Details"
copy["em-r-ps-9-c2"] = "Learn More"
copy["em-r-ps-9-c3"] = "Send Message"

# Creative #10: Didi Testimonial
copy["em-r-ps-10-p1"] = "Don&rsquo;t take our word for it. Didi went to Morocco with SALTY and came back different. Hear what they said about the surf, the food, the people, and why they&rsquo;d do it again tomorrow. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-r-ps-10-p2"] = "We could tell you Morocco is incredible. But Didi said it better. Real guest. Real experience. No script. SALTY Retreats. May 16&ndash;23. Limited spots. Message us on WhatsApp."
copy["em-r-ps-10-p3"] = "Didi booked Morocco not knowing what to expect. They left calling it the best week of their life. That&rsquo;s not marketing &mdash; that&rsquo;s what actually happens. SALTY Retreats. May 16&ndash;23."
copy["em-r-ps-10-h1"] = "Hear It from a Real Guest"
copy["em-r-ps-10-h2"] = "Didi&rsquo;s Morocco Experience"
copy["em-r-ps-10-h3"] = "The Best Week of Their Life"
copy["em-r-ps-10-c1"] = "Learn More"
copy["em-r-ps-10-c2"] = "See Trip Details"
copy["em-r-ps-10-c3"] = "Send Message"

# Creative #11: Cat Traer Testimonial
copy["em-r-ps-11-p1"] = "Cat went to SALTY Morocco and hasn&rsquo;t stopped talking about it since. The highlight? It wasn&rsquo;t one thing &mdash; it was everything. Hear her story. SALTY Retreats. May 16&ndash;23."
copy["em-r-ps-11-p2"] = "Cat didn&rsquo;t expect to love it this much. The surf surprised her. The food wrecked her. The people? She&rsquo;s still in the group chat 6 months later. SALTY Morocco. May 16&ndash;23."
copy["em-r-ps-11-p3"] = "Cat is coming back. That tells you everything you need to know. SALTY Retreats. Morocco. May 16&ndash;23. Hear why in her own words. Limited spots."
copy["em-r-ps-11-h1"] = "Why Cat Is Coming Back"
copy["em-r-ps-11-h2"] = "She Didn&rsquo;t Expect to Love It"
copy["em-r-ps-11-h3"] = "A Guest&rsquo;s Honest Take"
copy["em-r-ps-11-c1"] = "Learn More"
copy["em-r-ps-11-c2"] = "See Trip Details"
copy["em-r-ps-11-c3"] = "Send Message"

# ═══════════════════════════════════════════════
# MOF — VIDEO VIEWERS (substance + trust)
# ═══════════════════════════════════════════════

# Creative #12: Trip Details NA (Carousel)
copy["em-m-vv-12-p1"] = "You watched. Now here&rsquo;s what you get: 7 nights boutique riad in Taghazout. Daily surf coaching. Yoga + fitness. 3 meals a day. Medina tour. Airport transfers. Pro photography. All-inclusive. Limited to 20. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-m-vv-12-p2"] = "Here&rsquo;s what a week in Morocco actually looks like: wake up. Surf. Eat breakfast you&rsquo;ll dream about. Train. Yoga. Explore. Eat dinner on the rooftop. Repeat for 7 days. All-inclusive. SALTY Retreats. May 16&ndash;23."
copy["em-m-vv-12-p3"] = "Boutique riad, not a hotel chain. Surf coaches, not YouTube tutorials. Moroccan food, not a buffet. 20 people, not 200. This is travel done differently. SALTY Retreats. Morocco. May 16&ndash;23. From $2,150."
copy["em-m-vv-12-h1"] = "Here&rsquo;s What&rsquo;s Included"
copy["em-m-vv-12-h2"] = "7 Nights. Everything In."
copy["em-m-vv-12-h3"] = "The Full Breakdown"
copy["em-m-vv-12-c1"] = "See Trip Details"
copy["em-m-vv-12-c2"] = "Learn More"
copy["em-m-vv-12-c3"] = "Sign Up"

# Creative #14: Guest Reviews Carousel
copy["em-m-vv-14-p1"] = "We could tell you it&rsquo;s amazing. But they said it better: \"Best week of my life.\" \"I went solo and left with 15 new friends.\" \"Nothing comes close.\" Real guests. Real words. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-m-vv-14-p2"] = "7 retreats. Hundreds of guests. Here&rsquo;s what they keep saying: the surf was unreal. The food changed me. The people are why I&rsquo;m going back. SALTY Morocco. May 16&ndash;23. Limited to 20."
copy["em-m-vv-14-p3"] = "Find us a bad review. We&rsquo;ll wait. Guest after guest, retreat after retreat &mdash; same story: \"I didn&rsquo;t know travel could feel like this.\" SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-m-vv-14-h1"] = "What Guests Actually Say"
copy["em-m-vv-14-h2"] = "Read Their Words, Not Ours"
copy["em-m-vv-14-h3"] = "Zero Bad Reviews. Seriously."
copy["em-m-vv-14-c1"] = "Read Reviews"
copy["em-m-vv-14-c2"] = "Learn More"
copy["em-m-vv-14-c3"] = "See Trip Details"

# Creative #15: Cat Traer MOF (Video)
copy["em-m-vv-15-p1"] = "Cat went to Morocco with SALTY and came back changed. Not in a cheesy way. In a \"I forgot what it felt like to be this happy\" way. Hear her story. SALTY Retreats. May 16&ndash;23."
copy["em-m-vv-15-p2"] = "No scripts. No filters. Just Cat telling you what happened when she spent a week surfing, eating, and laughing with 19 strangers in Morocco. SALTY Retreats. May 16&ndash;23."
copy["em-m-vv-15-p3"] = "Cat was on the fence. Just like you. Then she went. And now she won&rsquo;t stop talking about it. SALTY Retreats. Morocco. May 16&ndash;23. 7 nights. All-inclusive."
copy["em-m-vv-15-h1"] = "Cat&rsquo;s Morocco Story"
copy["em-m-vv-15-h2"] = "From Skeptic to Superfan"
copy["em-m-vv-15-h3"] = "She Was on the Fence Too"
copy["em-m-vv-15-c1"] = "Learn More"
copy["em-m-vv-15-c2"] = "See Trip Details"
copy["em-m-vv-15-c3"] = "Send Message"

# Creative #16: Erin Recap (Video)
copy["em-m-vv-16-p1"] = "We just took 20 people to Morocco. Second time running this retreat. Honestly? Even better than the first. The surf was unreal. The food blew everyone away. The group? Nobody wanted to leave. We&rsquo;re going back. May 16&ndash;23."
copy["em-m-vv-16-p2"] = "I&rsquo;ve run retreats on four continents. Morocco keeps surprising me. The waves, the food, the riads &mdash; but mostly the people who show up. Every group becomes a family. SALTY Retreats. May 16&ndash;23."
copy["em-m-vv-16-p3"] = "Morocco 2025 set a new bar. Morocco 2026 is going to top it. Same incredible location. Same magic. Better programming. We want you there. SALTY Retreats. May 16&ndash;23. Limited to 20."
copy["em-m-vv-16-h1"] = "Even Better the Second Time"
copy["em-m-vv-16-h2"] = "Why I Can&rsquo;t Wait to Go Back"
copy["em-m-vv-16-h3"] = "Morocco Set a New Bar"
copy["em-m-vv-16-c1"] = "Watch More"
copy["em-m-vv-16-c2"] = "Learn More"
copy["em-m-vv-16-c3"] = "See Trip Details"

# Creative #17: Value for Money (Video)
copy["em-m-vv-17-p1"] = "Let&rsquo;s do the math. 7 nights accommodation: $700. Surf coaching: $400. Yoga + fitness: $350. All meals: $400. Excursions: $200. Transfers: $100. That&rsquo;s $2,150+ on your own. SALTY price: $2,150. Same trip. Zero planning. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-m-vv-17-p2"] = "$2,150 divided by 7 nights = $307/night. That includes your room, 3 meals a day, surf coaching, yoga, fitness, excursions, transfers, and photography. Find a better deal. We&rsquo;ll wait. SALTY Morocco. May 16&ndash;23."
copy["em-m-vv-17-p3"] = "A week at an all-inclusive resort: $2,500+ for a pool and a buffet. A week at SALTY Morocco: $2,150 for surf, yoga, real food, and 20 people who&rsquo;ll change your life. Easy math. May 16&ndash;23."
copy["em-m-vv-17-h1"] = "The Math Speaks for Itself"
copy["em-m-vv-17-h2"] = "$307/Night. Everything In."
copy["em-m-vv-17-h3"] = "Better Value Than a Resort"
copy["em-m-vv-17-c1"] = "See Pricing"
copy["em-m-vv-17-c2"] = "Learn More"
copy["em-m-vv-17-c3"] = "See Trip Details"

# ═══════════════════════════════════════════════
# MOF — WEBSITE VISITORS (they've browsed, give substance)
# ═══════════════════════════════════════════════

# Creative #12: Trip Details NA (Website Visitors)
copy["em-m-wv-12-p1"] = "You checked out the site. Here&rsquo;s the short version: 7 nights. Boutique riad. Daily surf coaching. Yoga + fitness. All meals. Excursions. Transfers. Photography. 20 guests max. SALTY Retreats. Morocco. May 16&ndash;23. From $2,150."
copy["em-m-wv-12-p2"] = "You browsed. Now let us paint the picture: sunrise surf in Taghazout. Moroccan tagine for lunch. Rooftop yoga. Dinner with 20 people who feel like family. Repeat for a week. All-inclusive. SALTY Retreats. May 16&ndash;23."
copy["em-m-wv-12-p3"] = "You had questions. We have answers. Everything&rsquo;s included: accommodation, coaching, food, excursions, and the kind of week that changes how you think about travel. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-m-wv-12-h1"] = "Everything You Wanted to Know"
copy["em-m-wv-12-h2"] = "The Short Version"
copy["em-m-wv-12-h3"] = "Your Questions, Answered"
copy["em-m-wv-12-c1"] = "See Trip Details"
copy["em-m-wv-12-c2"] = "Learn More"
copy["em-m-wv-12-c3"] = "Sign Up"

# Creative #14: Guest Reviews (Website Visitors)
copy["em-m-wv-14-p1"] = "Still thinking about it? These guests were too. Then they went: \"Best week of my life.\" \"Solo and left with 15 new friends.\" \"Hands down the best trip I&rsquo;ve ever taken.\" SALTY Morocco. May 16&ndash;23."
copy["em-m-wv-14-p2"] = "You&rsquo;ve seen the site. Now hear from the people who&rsquo;ve actually been. Every guest says the same thing: \"I wish I&rsquo;d booked sooner.\" SALTY Retreats. Morocco. May 16&ndash;23. Limited to 20."
copy["em-m-wv-14-p3"] = "The website shows you the trip. These reviews show you the feeling. \"Nothing comes close.\" \"Changed how I think about travel.\" \"Already booked my next one.\" SALTY Morocco. May 16&ndash;23."
copy["em-m-wv-14-h1"] = "Still Thinking? Read This."
copy["em-m-wv-14-h2"] = "They Were Curious Too"
copy["em-m-wv-14-h3"] = "See What Guests Say"
copy["em-m-wv-14-c1"] = "Read Reviews"
copy["em-m-wv-14-c2"] = "Learn More"
copy["em-m-wv-14-c3"] = "See Trip Details"

# Creative #15: Cat Traer MOF (Website Visitors)
copy["em-m-wv-15-p1"] = "You visited the site. Cat went to the retreat. Hear what she thinks about the surf, the food, the people, and whether it&rsquo;s worth it. Spoiler: she&rsquo;s going back. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-m-wv-15-p2"] = "Cat had the same questions you have. Is it worth it? Will I fit in? What&rsquo;s it actually like? She answered all of them after one week in Morocco. SALTY Retreats. May 16&ndash;23."
copy["em-m-wv-15-p3"] = "You&rsquo;ve read the website. Now hear from someone who lived it. Cat&rsquo;s Morocco story is the best sales pitch we never wrote. SALTY Retreats. May 16&ndash;23. All-inclusive."
copy["em-m-wv-15-h1"] = "She Had Your Questions Too"
copy["em-m-wv-15-h2"] = "From Website to Waitlist"
copy["em-m-wv-15-h3"] = "Cat Answered Them All"
copy["em-m-wv-15-c1"] = "Learn More"
copy["em-m-wv-15-c2"] = "See Trip Details"
copy["em-m-wv-15-c3"] = "Send Message"

# Creative #17: Value for Money (Website Visitors)
copy["em-m-wv-17-p1"] = "You saw the price. Here&rsquo;s what it covers: 7 nights accommodation. Daily surf coaching. Yoga + fitness. 3 meals/day. Excursions. Transfers. Photography. $2,150 all-inclusive. No surprises. SALTY Morocco. May 16&ndash;23."
copy["em-m-wv-17-p2"] = "Accommodation: $700. Surf coaching: $400. Yoga: $350. Meals: $400. Excursions + transfers: $300. Total separately: $2,150+. SALTY price: $2,150. Same everything. Zero hassle. May 16&ndash;23."
copy["em-m-wv-17-p3"] = "You&rsquo;ve been doing the research. Let us save you time: it&rsquo;s $2,150 all-inclusive. Everything. Room. Food. Coaching. Yoga. Excursions. Photography. The only extra is your flight. SALTY Morocco. May 16&ndash;23."
copy["em-m-wv-17-h1"] = "Here&rsquo;s What the Price Covers"
copy["em-m-wv-17-h2"] = "No Hidden Costs. Ever."
copy["em-m-wv-17-h3"] = "The Breakdown You Wanted"
copy["em-m-wv-17-c1"] = "See Pricing"
copy["em-m-wv-17-c2"] = "Learn More"
copy["em-m-wv-17-c3"] = "See Trip Details"

# ═══════════════════════════════════════════════
# MOF — ENGAGED FB/IG (warm social engagers)
# ═══════════════════════════════════════════════

# Creative #12: Trip Details NA (Engaged FB/IG)
copy["em-m-ef-12-p1"] = "You&rsquo;ve been liking our posts. Here&rsquo;s what you&rsquo;ve been liking: 7 nights in Morocco. Surf. Yoga. All meals. A crew of 20 who make it unforgettable. All-inclusive. SALTY Retreats. May 16&ndash;23. From $2,150."
copy["em-m-ef-12-p2"] = "Your feed brought you here. Now let us bring you to Morocco. 7 nights. Boutique riad. Daily surf coaching. Yoga + fitness. 3 meals/day. Excursions. 20 guests max. Everything included. May 16&ndash;23."
copy["em-m-ef-12-p3"] = "You engage with SALTY for a reason. It speaks to something. Morocco is where that something becomes real. 7 nights. Surf. Food. People. All-inclusive. May 16&ndash;23."
copy["em-m-ef-12-h1"] = "Turn Your Likes Into a Trip"
copy["em-m-ef-12-h2"] = "From Your Feed to Morocco"
copy["em-m-ef-12-h3"] = "This Is What You&rsquo;ve Been After"
copy["em-m-ef-12-c1"] = "See Trip Details"
copy["em-m-ef-12-c2"] = "Learn More"
copy["em-m-ef-12-c3"] = "Sign Up"

# Creative #14: Guest Reviews (Engaged FB/IG)
copy["em-m-ef-14-p1"] = "You&rsquo;ve seen our content. Now hear from the people who&rsquo;ve lived it: \"Best week of my life.\" \"Went solo, left with a crew.\" \"Already planning my next one.\" Real guests. SALTY Morocco. May 16&ndash;23."
copy["em-m-ef-14-p2"] = "The content got your attention. The reviews should seal the deal. Every guest says the same thing: it&rsquo;s better than it looks. And it looks damn good. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-m-ef-14-p3"] = "You liked the posts. They lived the trip. \"Nothing comes close.\" \"The food ruined restaurants for me.\" \"Why didn&rsquo;t I do this sooner?\" SALTY Morocco. May 16&ndash;23. Limited to 20."
copy["em-m-ef-14-h1"] = "From Liking to Booking"
copy["em-m-ef-14-h2"] = "It&rsquo;s Better Than It Looks"
copy["em-m-ef-14-h3"] = "Hear It From Them"
copy["em-m-ef-14-c1"] = "Read Reviews"
copy["em-m-ef-14-c2"] = "Learn More"
copy["em-m-ef-14-c3"] = "See Trip Details"

# Creative #16: Erin Recap (Engaged FB/IG)
copy["em-m-ef-16-p1"] = "You follow us. So you&rsquo;ve seen the highlights. But here&rsquo;s what the camera didn&rsquo;t catch: the late-night rooftop chats. The tears on the last day. The group chat that&rsquo;s still going 6 months later. SALTY Morocco. May 16&ndash;23."
copy["em-m-ef-16-p2"] = "Erin just got back from taking 20 people to Morocco. Her honest take? Better than the first time. The surf, the food, the people &mdash; Morocco keeps raising the bar. May 16&ndash;23."
copy["em-m-ef-16-p3"] = "Behind every post is a real week with real people. Erin runs these retreats because she genuinely gives a damn. Morocco 2026 is going to be special. May 16&ndash;23. Limited to 20."
copy["em-m-ef-16-h1"] = "What the Camera Didn&rsquo;t Catch"
copy["em-m-ef-16-h2"] = "Erin&rsquo;s Honest Take"
copy["em-m-ef-16-h3"] = "Behind the Posts"
copy["em-m-ef-16-c1"] = "Watch More"
copy["em-m-ef-16-c2"] = "Learn More"
copy["em-m-ef-16-c3"] = "See Trip Details"

# ═══════════════════════════════════════════════
# BOF — LANDING PAGE VIEWERS (final push, WhatsApp CTA)
# ═══════════════════════════════════════════════

# Creative #18: Itinerary Video (Video / 30-45s)
copy["em-b-lv-18-p1"] = "You&rsquo;ve seen the page. Here&rsquo;s everything you get: 7 nights boutique riad. Surf coaching daily. Yoga + fitness. 3 meals/day. Medina tour. Airport transfers. Photography. Welcome kit. Nothing extra to pay. SALTY Morocco. May 16&ndash;23. Message us."
copy["em-b-lv-18-p2"] = "No hidden costs. No add-ons. No \"that&rsquo;s extra.\" Your room, all meals, surf coaching, yoga, fitness, excursions, transfers, and photography &mdash; all included. That&rsquo;s SALTY. Morocco. May 16&ndash;23. WhatsApp us any questions."
copy["em-b-lv-18-p3"] = "Let&rsquo;s get specific. Boutique riad in Taghazout. Surf coaching with certified instructors. Vinyasa yoga. Functional fitness. Moroccan home cooking. Guided medina tour. Both-way transfers. Professional photos of your best week. SALTY Retreats. May 16&ndash;23."
copy["em-b-lv-18-h1"] = "Everything&rsquo;s Included. Everything."
copy["em-b-lv-18-h2"] = "No Surprises. No Add-Ons."
copy["em-b-lv-18-h3"] = "Here&rsquo;s Exactly What You Get"
copy["em-b-lv-18-c1"] = "Message Us on WhatsApp"
copy["em-b-lv-18-c2"] = "Send Message"
copy["em-b-lv-18-c3"] = "Book Now"

# Creative #19: Morocco Vlog (Video / 45-90s)
copy["em-b-lv-19-p1"] = "No scripts. No actors. No filters. This is what 7 days in Morocco with SALTY actually looks like. Real people. Real moments. Real friendships. A few spots left. May 16&ndash;23. Message us."
copy["em-b-lv-19-p2"] = "Two years of footage. Hundreds of real moments. This is the trip &mdash; unedited, unscripted, and exactly what you&rsquo;ll get. SALTY Morocco. May 16&ndash;23. Message us on WhatsApp."
copy["em-b-lv-19-p3"] = "Hit play. That&rsquo;s your week. Sunrise surf. Beach training. Rooftop dinners. 20 strangers becoming family. This is SALTY Morocco. May 16&ndash;23. A few spots left."
copy["em-b-lv-19-h1"] = "This Is the Real Thing"
copy["em-b-lv-19-h2"] = "No Script. No Filter."
copy["em-b-lv-19-h3"] = "Your Week, Unedited"
copy["em-b-lv-19-c1"] = "Message Us"
copy["em-b-lv-19-c2"] = "Send Message"
copy["em-b-lv-19-c3"] = "Book Now"

# Creative #20: Pricing Plans (Carousel)
copy["em-b-lv-20-p1"] = "Shared room: $2,150 ($307/night). Private room: $2,650 ($378/night). Everything included. Payment plans available. $500 deposit holds your spot. SALTY Retreats. Morocco. May 16&ndash;23. Message us."
copy["em-b-lv-20-p2"] = "$2,150 for 7 nights. Room. All meals. Surf coaching. Yoga. Fitness. Excursions. Transfers. Photography. That&rsquo;s $307/night for the best week of your year. Payment plans available. SALTY Morocco. May 16&ndash;23."
copy["em-b-lv-20-p3"] = "Two options. Shared: $2,150. Private: $2,650. Both include everything. Both include the trip of a lifetime. $500 deposit. Payment plans. No excuses left. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-b-lv-20-h1"] = "Pricing Made Simple"
copy["em-b-lv-20-h2"] = "$307/Night. Everything In."
copy["em-b-lv-20-h3"] = "Payment Plans Available"
copy["em-b-lv-20-c1"] = "Message Us on WhatsApp"
copy["em-b-lv-20-c2"] = "Book Now"
copy["em-b-lv-20-c3"] = "Send Message"

# Creative #21: Day-by-Day Itinerary (Carousel)
copy["em-b-lv-21-p1"] = "Day 1: Arrive. Sunset yoga. Welcome dinner. Days 2&ndash;3: Surf + train + explore. Day 4: Rest day, medina, hammam. Days 5&ndash;6: Surf + fitness + rooftop dinners. Day 7: Last surf. Group photo. Farewell dinner. Every day flexible. Nothing mandatory. SALTY Morocco."
copy["em-b-lv-21-p2"] = "Structure when you want it. Freedom when you need it. Every day has programming &mdash; surf, yoga, training, excursions. But there&rsquo;s always time to nap, explore, or just sit on the roof with a coffee. May 16&ndash;23."
copy["em-b-lv-21-p3"] = "Typical day: 7am surf. 10am breakfast. 12pm train. 2pm free time. 5pm yoga. 7pm dinner. 9pm rooftop. Midnight sleep. Wake up and do it again. SALTY Morocco. May 16&ndash;23. Message us for the full schedule."
copy["em-b-lv-21-h1"] = "Your Week, Day by Day"
copy["em-b-lv-21-h2"] = "Structure + Freedom"
copy["em-b-lv-21-h3"] = "See the Full Schedule"
copy["em-b-lv-21-c1"] = "Get Full Itinerary"
copy["em-b-lv-21-c2"] = "Message Us"
copy["em-b-lv-21-c3"] = "Send Message"

# Creative #22: Ask Us a Question (Nate to Camera)
copy["em-b-lv-22-p1"] = "On the fence? I get it. It&rsquo;s a big trip. So here&rsquo;s what I&rsquo;ll say: just message us. No pitch. No pressure. No bots. You&rsquo;ll talk to me or Erin. We&rsquo;ve answered every question you can think of. WhatsApp or DM. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-b-lv-22-p2"] = "You&rsquo;re not messaging a chatbot. You&rsquo;re talking to me &mdash; Nate. Or Erin. The actual humans who run these retreats. Ask about surf levels, pricing, roommates, what to pack, whether you&rsquo;ll make friends solo. We reply within hours. SALTY Morocco."
copy["em-b-lv-22-p3"] = "Got questions? Good. That means you&rsquo;re interested. Shoot us a message on WhatsApp. No sales pitch. No automated nonsense. Just honest answers from the people who built this trip. SALTY Retreats. Morocco. May 16&ndash;23."
copy["em-b-lv-22-h1"] = "Just Ask. We&rsquo;ll Answer."
copy["em-b-lv-22-h2"] = "Talk to a Real Human"
copy["em-b-lv-22-h3"] = "No Pitch. Just Answers."
copy["em-b-lv-22-c1"] = "Message Us on WhatsApp"
copy["em-b-lv-22-c2"] = "Send Message"
copy["em-b-lv-22-c3"] = "Contact Us"

# ═══════════════════════════════════════════════
# BOF — HIGH-INTENT 14D (hottest audience, close the deal)
# ═══════════════════════════════════════════════

# Creative #20: Pricing Plans (High-Intent)
copy["em-b-hi-20-p1"] = "You&rsquo;ve been looking at this for two weeks. Here&rsquo;s the pricing: Shared: $2,150. Private: $2,650. Everything included. Payment plans available. $500 holds your spot. SALTY Morocco. May 16&ndash;23. Message us."
copy["em-b-hi-20-p2"] = "You keep coming back to this page. We get it &mdash; it&rsquo;s a decision. So here&rsquo;s everything: $2,150 shared, $2,650 private. All-inclusive. Payment plans. $500 deposit. No hidden costs. SALTY Morocco. May 16&ndash;23."
copy["em-b-hi-20-p3"] = "Still here? Good. Shared room: $307/night all-inclusive. Private room: $378/night all-inclusive. Both include everything. Payment plans make it easy. One message starts the process. SALTY Morocco."
copy["em-b-hi-20-h1"] = "You&rsquo;ve Been Thinking About It"
copy["em-b-hi-20-h2"] = "The Decision Made Easy"
copy["em-b-hi-20-h3"] = "Two Options. One Amazing Week."
copy["em-b-hi-20-c1"] = "Message Us on WhatsApp"
copy["em-b-hi-20-c2"] = "Book Now"
copy["em-b-hi-20-c3"] = "Send Message"

# Creative #21: Day-by-Day Itinerary (High-Intent)
copy["em-b-hi-21-p1"] = "You want to know exactly what you&rsquo;re signing up for. We respect that. Every day mapped out: surf, yoga, training, excursions, free time, rooftop dinners. Nothing mandatory. Everything incredible. SALTY Morocco. May 16&ndash;23."
copy["em-b-hi-21-p2"] = "The schedule: sunrise surf, morning training, afternoon free, sunset yoga, rooftop dinner. Repeat for 7 days. Mix in a medina tour and a hammam. All flexible. All included. May 16&ndash;23."
copy["em-b-hi-21-p3"] = "Day 1: arrive, unpack, breathe. Day 7: leave wondering how 20 strangers became your closest friends in a week. Everything in between? Surf, yoga, fitness, food, and stories you&rsquo;ll tell for years. SALTY Morocco."
copy["em-b-hi-21-h1"] = "Every Day. Mapped Out."
copy["em-b-hi-21-h2"] = "Here&rsquo;s What You Sign Up For"
copy["em-b-hi-21-h3"] = "7 Days That Change Everything"
copy["em-b-hi-21-c1"] = "Get Full Itinerary"
copy["em-b-hi-21-c2"] = "Message Us"
copy["em-b-hi-21-c3"] = "Book Now"

# Creative #22: Ask Us a Question (High-Intent)
copy["em-b-hi-22-p1"] = "You&rsquo;ve been on this page more than once. You&rsquo;ve got questions. We&rsquo;ve got answers. Message us on WhatsApp &mdash; you&rsquo;ll talk to Nate or Erin. The actual people behind SALTY. No pitch. Within the hour. May 16&ndash;23."
copy["em-b-hi-22-p2"] = "The only thing between you and Morocco is one message. Surf levels? We&rsquo;ve taught beginners who caught waves on day one. Solo? 67% of our guests come alone. Budget? We have payment plans. Message us. SALTY Retreats."
copy["em-b-hi-22-p3"] = "We know you&rsquo;ve been looking. We know you&rsquo;ve got questions. Here&rsquo;s the easiest next step: send us a WhatsApp. We answer every single one. Personally. Within hours. No pressure. SALTY Morocco. May 16&ndash;23."
copy["em-b-hi-22-h1"] = "One Message Away"
copy["em-b-hi-22-h2"] = "Your Questions. Our Answers."
copy["em-b-hi-22-h3"] = "We Know You&rsquo;re Interested"
copy["em-b-hi-22-c1"] = "Message Us on WhatsApp"
copy["em-b-hi-22-c2"] = "Send Message"
copy["em-b-hi-22-c3"] = "Contact Us"


# ─────────────────────────────────────────────
# INJECTION ENGINE
# ─────────────────────────────────────────────

def inject_copy(html_content, copy_dict):
    """Replace innerHTML of contenteditable fields by data-key."""
    updated = 0
    missing = []

    for key, content in copy_dict.items():
        # Match: data-key="KEY" data-placeholder="...">ANYTHING</div>
        pattern = rf'(data-key="{re.escape(key)}" data-placeholder="[^"]*">)(.*?)(</div>)'
        match = re.search(pattern, html_content)
        if match:
            html_content = re.sub(
                pattern,
                lambda m, c=content: m.group(1) + c + m.group(3),
                html_content,
                count=1
            )
            updated += 1
        else:
            missing.append(key)

    return html_content, updated, missing


def main():
    html_path = os.path.join(os.path.dirname(__file__), "campaign", "index.html")

    print(f"Reading {html_path}...")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    print(f"Injecting {len(copy)} copy fields...")
    html, updated, missing = inject_copy(html, copy)

    print(f"\nResults:")
    print(f"  Updated: {updated}")
    print(f"  Missing: {len(missing)}")
    if missing:
        print(f"  Missing keys:")
        for k in missing:
            print(f"    - {k}")

    # Write back
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\nDone! {updated} fields written to {html_path}")


if __name__ == "__main__":
    main()
