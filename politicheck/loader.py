# coding=utf-8

from __future__ import division
import os,pickle,pprint
import re
from collections import Counter

def words(text): return re.findall('[a-z]+', text.lower())

def Dfs(corpus):
    """calculate the document frequency for all terms in the corpus"""
    cnt = Counter()
    for d in corpus:
        s = set(d['bag'])
        for word in s:
            cnt[word] += 1
    return cnt

path = os.getcwd()
f_scraped = os.path.join(path,'scraper_output_1437237126.pickle')
#f_scraped = os.path.join(path,'scraper_output.pickle')

f = open(f_scraped,'rb')
statements = pickle.load(f)
f.close()

raw_text = """Fairfax, Virginia (CNN)Hours after the Supreme Court legalized same-sex marriage in all 50 states, Hillary Clinton told hundreds of Virginia Democrats on Friday that "Across the board, (Republicans) are the party of the past, not the future."

The Democratic frontrunner was speaking at a Jefferson Jackson fundraiser for the Virginia Democratic Party at George Mason University on a night in which she was repeatedly referred to by fellow Democrats as the next President of the United States.

RELATED: The week that changed the nation
Obergefell: &#39;What a wonderful legacy for my husband&#39;

Obergefell: 'What a wonderful legacy for my husband' 04:19
PLAY VIDEO

"This morning, they all decried the Supreme Court's ruling," Clinton said, noting that "we even heard them call for a constitutional amendment" against same-sex marriage.

A fired-up Clinton then seemingly spoke directly at the 13 declared Republican presidential hopefuls.

"I am asking them, please, don't make the rights, the hopes, of any American into a political football for this 2016 campaign," she said. "LGBT Americans should be free not just to marry, but to live, learn and work, just like everybody else."

Republican response to the Supreme Court's decision was universally opposed, but politically mixed. Former Florida Gov. Jeb Bush called for respect for the court's decision, despite opposing it. On the other side of the spectrum, Louisiana Gov. Bobby Jindal said he wants to amend the Constitution to leave the decision over who can marry up to each state.

Clinton read the last paragraph of Justice Anthony Kennedy's opinion from the stage on Friday, ending with, "And to that I say, amen, thank you."

"This morning, love triumphed in the highest court in our land," Clinton said. "Equality triumphed, America triumphed."

RELATED: How the GOP triumphed on same-sex marriage
Our nation&#39;s response to a historic decision

Our nation's response to a historic decision 01:14
PLAY VIDEO

She did not mention former Maryland Gov. Martin O'Malley, former Rhode Island Gov. Lincoln Chafee or Vermont Sen. Bernie Sanders during the event, all of whom are vying to be the Democratic Party's nominee.

Clinton's stance on same-sex marriage has evolved over the years. Her husband, President Bill Clinton, signed the Defense of Marriage Act in 1996, which defined for federal purposes marriage between one man and one woman. As a senator, Clinton backed civil unions and partner benefits for same-sex couples, and came out in favor of same-sex marriage in 2013, shortly before the Court struck down a key provision of the 1996 law.

But the former secretary of state's attacks on Republican hopefuls were not limited to same-sex marriage.

Reacting to the other landmark decision by the Supreme Court this week, Clinton said, "All the Republican candidates were furious that earlier this week the Supreme Court once again confirmed what we have all known and believed for years: (Obamacare) is settled law and it is here to stay."

In a 6-3 decision, the Supreme Court saved Obama's controversial health care law on Thursday, ruling that the Affordable Care Act was authorized to provide federal tax credits to states with federal marketplaces.

"Even after two Supreme Court verdicts and a presidential election, they are still fighting to take us backwards," Clinton said, referring to the 2012 Supreme Court decision on the issue and that year's presidential election. "I think we can sum up the message from the Court and the American people: 'Move on.'"

As she has in the past, Clinton said she doesn't think the health care law is perfect, pointing to drug and out-of-pocket costs as two areas that she says need to be addressed.

But she embraced Obama throughout the speech, and she applauded the way the President eulogized Rev. Clementa Pinckney, the South Carolina state senator who was killed along with eight others in last week's church massacre in Charleston, South Carolina.

RELATED: White House shines rainbow colors to hail marriage ruling

She referenced the tragedy when she hit House Republicans for voting on Wednesday to put restrictions on whether the Centers for Disease Control and Prevention can study gun violence and make recommendations.

"How can you watch massacre after massacre and take that vote?" she asked. "That is wrong. It puts our people at risk, and I, for one, am never going to stop fighting for a better, safer approach to get the gun violence in this country under control."
U.S. 21st country to allow same-sex marriage nationwide

U.S. 21st country to allow same-sex marriage nationwide 02:20
PLAY VIDEO

Friday's event was meant to focus on the successes of Virginia Democrats -- including longtime Clinton friend and Virginia Gov. Terry McAuliffe. But as the program went on, the event started to feel like a Hillary for America rally.

Rep. Bobby Scott said he was happy to welcome "the next President of the United States of America to the commonwealth of Virginia." Sen. Tim Kaine said, "I'm so excited we get to be here to welcome Secretary Clinton, our next President." And Sen. Mark Warner added, "I don't know about you, but I made my choice. I'm ready for Hillary."

McAuliffe, Clinton's 2008 campaign chairman, was even more effusive, to the point of getting personal.

"Folks, let me say this, this is personal for me," he said. "I have known Hillary for decades. We have worked hard together, we have played hard together."

The famously blunt governor went on to tell the audience that when he and his wife travel with Bill and Hillary Clinton and the governor wants a drink, "I don't go looking for Bill Clinton. I go looking for Hillary Clinton, because she is a lot more fun that Bill Clinton."

McAuliffe described Clinton as a fighter who has "been knocked down" but gets up every time and "gets right back in that arena again."

"And yes, after 239 years," he concluded, "it is time for a woman President of the United States."""
########################################################
raw_text_2 = u"""Massachusetts Sen. Elizabeth Warren drew a red line on Friday for 2016 presidential candidates, calling for them to commit to end the so-called “revolving door” between Wall Street and the Cabinet.

The firebrand populist said specifically that all the presidential candidates should support Wisconsin Sen. Tammy Baldwin’s bill introduced this week that would prohibit bonuses for Wall Street executives who take government jobs.

“Anyone who wants to be President should appoint only people who have already demonstrated they are independent, who have already demonstrated that they can hold giant banks accountable,” said Warren, speaking in Phoenix at Netroots Nation, a convention of liberal activists.

While the call to action was aimed at everyone running in 2016, its clearest target was Democratic frontrunner Hillary Clinton, who is courting the very types of progressive activists in the audience in both the primary and general election.

MORE: How Elizabeth Warren’s Populist Fury is Remaking Democratic Politics

While Warren declined to run for president, her supporters give her credit for pushing Clinton to the left and setting the liberal standard on a host of issues.

Clinton has already gone at least part of the way to satisfying Warren’s demands. During a speech Monday on her vision for the American economy, Clinton called for greater regulation of financial institutions.

“I will appoint and empower regulators who understand that Too Big To Fail is still too big a problem,” Clinton said on Monday. She outlined plans to rein in Wall Street and “go beyond Dodd-Frank.”

Baldwin’s bill is aimed at addressing what progressives see as a profound governmental problem: that government finance appointees often have close ties to Wall Street. In her speech, Warren pointed out that three of the last four Treasury Secretaries, the vice chair of the Federal Reserve and other key government officials have had close ties with Citigroup, a major Wall Street bank.

“Elizabeth Warren offered a framework for how Democratic presidential candidates can reduce Wall Street influence in key appointments,” said Stephanie Taylor, co-founder of the Progressive Change Campaign Committee after Warren’s speech.

Unhappy with President Obama’s less aggressive approach to Wall Street, the Democratic left has searched for a liberal champion who can address issues like income inequality and campaign finance reforms and found some of its voice in Warren, a former Harvard law professor and consumer protection advocate.

While Clinton has rhetorically embraced much of Warren’s logic, she has not gone as far as her fellow Democratic presidential candidates, Vermont Sen. Bernie Sanders and former Maryland Gov. Martin O’Malley.


O’Malley called earlier this month for appointing regulatory officials who had for at least three years not worked in the financial sector and would be willing to prosecute criminal financial cases, laying out a detailed plan to regulate Wall Street with much of the same language Warren has used.

In her speech Friday, Warren spoke about a surging progressive movement across the country, calling Washington, D.C., out of touch with the rest of America.

She ticked off a litany of issues that she said Americans are further to the left on than elected officials, including raising the minimum wage, reducing the cost of college, requiring paid sick leave, increasing social security benefits, and enacting campaign finance reform.

“I’m here to make an announcement to insider Washington: America is far more progressive than you are,” Warren said.

It’s a message Warren is counting on resonating in the 2016 election. Warren added that the economic crisis in 2008 would have been different if there had been left-leaning economists in high governmental positions instead of Wall Street alums.

“How would the world be different today if, when the economic crisis hit [in 2008], Joe Stiglitz had been Secretary of the Treasury?” Warren said.

Stiglitz is now advising Hillary Clinton."""

len_limit = 3
article_bag = [w for w in words(raw_text_2) if len(w) > len_limit]
#create statement bags
proc = [{'statement':s,'bag':[w for w in words(s[2]+' '+s[3]) if len(w) > len_limit]} for s in statements[0:200]]

dfreqs = Dfs(proc)
print dfreqs.most_common(10)

# calculate score
def score(bag, score_bag):
    #sb = set(bag)
    #ssb = set(score_bag)
    #s = sb.intersection(ssb)
    #tot = 0.0
    #for w in s:
    #    tot+=1/dfreqs[w]
    #return tot
    return len([b for b in bag if b in score_bag])/float(len(bag))

def score_dist(source,text):
    pass


for p in proc:
    p['score'] = score(p['bag'],article_bag)

print 'sorting'
#find some high-scoring things
proc.sort(key=lambda p:p['score'])
proc.reverse()

for p in proc[0:5]:
    print p['score'],p['statement'][2]+': '+p['statement'][3]
