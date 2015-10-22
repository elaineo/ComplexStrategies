verbs = ['buy','sell','accumulate','go long on','take a short position in','backfill','corner the market in','rotate holdings into','take a position against','average down on','acquire','open an outsized position in','take a short interest in','average up on','enter a bracketed sell order on','short hedge']

adjs = ['asset-sensitive','tightening','above-par','at-par','unauthorized','below-par','unsecured','asset-backed',
'collateralized','contingent','deferred','conditional','callable','convertible',
'discounted','fixed-for-floating','highly-leveraged','overbought','oversold',
'thinly-traded']

nouns1 = ['commercial paper','accrual bonds',
'balance sheet CDOs','barrier options','binary options','bear spreads','bull spreads','butterfly spreads','emerging market debt',
'belly tranches','Brady bonds','bond obligations', 'debt obligations',
'loan obligations','closed-end mortgage bonds','mortgage obligations',
'credit default swaps','synthetic CDOs','intercommodity spreads','pork belly futures', 
'interest rate swaps','inverse floaters','liability swaps',
'mezzanine tranches','mortgage-backed securities',
'nonlinear derivatives','OTC pink sheets','PAC bonds', 
'planned amortization bonds','prior lien bonds','quanto swaps','ratchet options','refunded bonds',
'revenue bonds','split-coupon bonds','swaptions','total return swaps'
,'vanilla swaps','zero-coupon bonds','balloon options',
'subprime loans','Bermuda options','call swaptions','exotic currency warrants','Asian options','illiquid options','underwater mortgages','immediate-term bonds','toxic subprime mortgages']
nouns2 = ['accrued-coupon bonds','adjustable-rate preferred Groupon shares','auction rate securities','preferred AIG stock','natural gas forward spreads',
'Eurobonds','Eurodollar bundles','Eurosterling futures', 'platinum futures',
'extendable YHOO call options', 'Bear Stearns junk bonds','Detroit municipal bonds',
'participating preferred AAPL stock','Dutch tulip bulbs',
'short-term Treasury bills','Treasury Inflation-Protected Securities','total return swaps','negative-return Treasury bonds','agricultural commodities','bitcoins','exotic currency futures','laundered Mexican Pesos',
'Greek Drachma on the black market','base metal futures','crude oil futures',
'S&P 500 futures','toxic subprime mortgages','Salomon Brothers World Equity Index futures']

using = ['antithetic variates','an autoregressive process',
'the absolute pricing model','alpha transport','dynamic hedging',
'autocorrelation','autoregressive conditional heteroskedacity',
'an autoregressive moving-average process','the Black-Scholes pricing model','CAPM',
'the Cauchy distribution','Cholesky factorization','the Cornish-Fisher expansion',
'a delta-gamma approximation','STARC bands',
'a deterministic volatility function model','duration-convexity matching',
'Garman and Kohlhager pricing','gradient approximation',
'homoskedacity','Gaussian noise','interpolation remapping','the KMV model',
'leptokurtosis','a local volatility model','those guys from Long Term Capital Management','a moving-average process','the Merton model','the Monte Carlo method','a negative semidefinite matrix','ordinary least squares','pairs trading','passive investing','principal component analysis','perfected interest','portfolio remapping',
'professional indemnity insurance','a ratings transition matrix','a reduced form model','a regime switching model','rehypothecation', 'a relative pricing model',
'insider trading','secured debt','self-regulation under the supervision of the SEC',
'a perfectly efficient market','the separation theorem','a Ponzi scheme','a short squeeze','a shell corporation in Belize','naked shorts',
'spline interpolation','a stable Paretian distribution','statistical arbitrage','a stochastic volatility model','stop-loss limits','a supermartingale','a structural credit risk model','offshore bank accounts','the Wiener process','attribution analysis','an autoregressive integrated moving average','accumulation/distribution indicators','a Golden Cross', 'the Arms index','the accumulative swing index','the Aroon indicator','an ascending channel','countertrend strategies',
'Gold\'s Death Cross', 'Bollinger bands','synthetic puts','the VWAP cross',
'Andrew\'s Pitchfork','Coppock Guides','a dedicated short bias',
'DuPont analysis','Bayesian approximations','Fibonacci clusters','fictitious credit',
'forced liquidation','fuzzy logic','Forex pivot points','Forex scalping','Gartley patterns','an iceberg order','lagging indicators','magic formula investing','manual execution','parabolic indicators','Phi ellipses','quote stuffing','The Big Mac index','accreting principal swaps','negative carry pairs','triangular currency arbitrage','piercing patterns','impulse wave patterns','polarized fractal efficiency','swap transferring risk with participating elements']

to = ['monetize','capitalize on','leverage','exploit','profit from',
'hedge','offset','securitize','micro-hedge','optimize for','maximize the effects of','minimize the effects of','derive profits from','maximize return on']

nouns3 = ['alpha','asset-backed securities','dollar volume liquidity','low volume pullback','a hook reversal','retracement',
'back-end loads','a Cyprus bank run','a Swiss bank run','a Norwegian bank run',
'basis risk','rigged Libor rates','beta','cash flow risk','counterparty risk','covariance stationarity','the crack spread','the discount factor','gamma exposure',
'the effective Fed funds rate','a debt-for-equity swap','Euro interbank offered rates','expected default frequency','gains trading','gamma',
'asset-liability risk','arbitrage conditions','volatility','default intensity',
'the hazard rate','Herstatt risk','impact costs','interest rate spreads','intrinsic value','kappa','London interbank bid rates','Libor-swap curves',
'liquidity spread','the Macaulay duration','a margin call','maximum likely exposure',
'mean reversion','volatility skew','the singularity','downside risk',
'black swan events','nominal yield','parametric VaR','potential exposure','pre-settlement risk','a downgrade of UK\'s credit rating',
'Twitter\'s upcoming IPO','repricing risk','required capital','risk-adjusted return on capital','rollover risk','an upcoming accounting scandal','a low Sharpe ratio',
'Jensen\'s alpha','specific risk','systematic risk','Treasury-Eurodollar spreads',
'the Treynor ratio','the US unemployment rate','QE4','unexpected loss',
'an Asian Financial Crisis','another housing bubble','insufficient Federal stimulus','Greek austerity measures','a flash crash','an exhaustion gap','involuntary bankruptcy','uncovered interest rate parity','dollar devaluation','the bail-out of Cyprus','an in-house rogue trader','the fiscal cliff','a housing recovery','current account deficits','the collapse of the Treasury bond market','easy money','deteriorating fundamentals','a return to socialism','a SARS outbreak','global warming','the collapse of China\'s economy','a deflationary spiral']