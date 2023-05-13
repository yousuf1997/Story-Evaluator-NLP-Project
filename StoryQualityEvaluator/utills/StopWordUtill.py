
'''
    This class represents stop words dictionary, and has functionality to check a word belongs to stop words
    source of the words : https://countwordsfree.com/stopwords
'''

class StopWordsUtill:
    def __init__(self):
        self._stopWordList = [];
        self._buildStopWordMap()

    def test(self):
        self._stopWordList = ['a', 'an', 'the', 'and', 'but', 'or', 'as', 'at', 'by', 'for', 'in', 'of', 'on', 'to', 'up', 'with']
    def stopInit(self):
        self._stopWordList = ['call','s' ,'upon', 'still', 'nevertheless', 'down', 'every', 'forty', '‘re', 'always', 'whole', 'side', "n't", 'now', 'however', 'an', 'show', 'least', 'give', 'below', 'did', 'sometimes', 'which', "'s", 'nowhere', 'per', 'hereupon', 'yours', 'she', 'moreover', 'eight', 'somewhere', 'within', 'whereby', 'few', 'has', 'so', 'have', 'for', 'noone', 'top', 'were', 'those', 'thence', 'eleven', 'after', 'no', '’ll', 'others', 'ourselves', 'themselves', 'though', 'that', 'nor', 'just', '’s', 'before', 'had', 'toward', 'another', 'should', 'herself', 'and', 'these', 'such', 'elsewhere', 'further', 'next', 'indeed', 'bottom', 'anyone', 'his', 'each', 'then', 'both', 'became', 'third', 'whom', '‘ve', 'mine', 'take', 'many', 'anywhere', 'to', 'well', 'thereafter', 'besides', 'almost', 'fifteen', 'towards', 'none', 'be', 'herein', 'two', 'using', 'whatever', 'please', 'perhaps', 'full', 'ca', 'we', 'latterly', 'here', 'therefore', 'us', 'how', 'was', 'made', 'the', 'or', 'may', '’re', 'namely', "'ve", 'anyway', 'amongst', 'used', 'ever', 'of', 'there', 'than', 'why', 'really', 'whither', 'in', 'only', 'wherein', 'last', 'under', 'own', 'therein', 'go', 'seems', '‘m', 'wherever', 'either', 'someone', 'up', 'doing', 'on', 'rather', 'ours', 'again', 'same', 'over', '‘s', 'latter', 'during', 'done', "'re", 'put', "'m", 'much', 'neither', 'among', 'seemed', 'into', 'once', 'my', 'otherwise', 'part', 'everywhere', 'never', 'myself', 'must', 'will', 'am', 'can', 'else', 'although', 'as', 'beyond', 'are', 'too', 'becomes', 'does', 'a', 'everyone', 'but', 'some', 'regarding', '‘ll', 'against', 'throughout', 'yourselves', 'him', "'d", 'it', 'himself', 'whether', 'move', '’m', 'hereafter', 're', 'while', 'whoever', 'your', 'first', 'amount', 'twelve', 'serious', 'other', 'any', 'off', 'seeming', 'four', 'itself', 'nothing', 'beforehand', 'make', 'out', 'very', 'already', 'various', 'until', 'hers', 'they', 'not', 'them', 'where', 'would', 'since', 'everything', 'at', 'together', 'yet', 'more', 'six', 'with', 'thereupon', 'becoming', 'around', 'due', 'keep', 'somehow', 'n‘t', 'across', 'all', 'when', 'i', 'empty', 'nine', 'five', 'get', 'see', 'been', 'name', 'between', 'hence', 'ten', 'several', 'from', 'whereupon', 'through', 'hereby', "'ll", 'alone', 'something', 'formerly', 'without', 'above', 'onto', 'except', 'enough', 'become', 'behind', '’d', 'its', 'most', 'n’t', 'might', 'whereas', 'anything', 'if', 'her', 'via', 'fifty', 'is', 'thereby', 'twenty', 'often', 'whereafter', 'their', 'also', 'anyhow', 'cannot', 'our', 'could', 'because', 'who', 'beside', 'by', 'whence', 'being', 'meanwhile', 'this', 'afterwards', 'whenever', 'mostly', 'what', 'one', 'nobody', 'seem', 'less', 'do', '‘d', 'say', 'thus', 'unless', 'along', 'yourself', 'former', 'thru', 'he', 'hundred', 'three', 'sixty', 'me', 'sometime', 'whose', 'you', 'quite', '’ve', 'about', 'even', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def _buildStopWordMap(self):
        self._stopWordList = ["able" ,"about" ,"above" ,"abroad" ,"according" ,"accordingly" ,"across" ,"actually", "'"
            ,"adj" ,"after" ,"afterwards" ,"again" ,"against" ,"ago" ,"ahead" ,"ain't" ,"all" ,"allow"
            ,"allows" ,"almost" ,"alone" ,"along" ,"alongside" ,"already" ,"also" ,"although"
            ,"always" ,"am" ,"amid" ,"amidst",
                              "among" ,"amongst" ,"an" ,"and" ,"another" ,"any" ,"anybody" ,"anyhow" ,"anyone"
            ,"anything" ,"anyway" ,"anyways" ,"anywhere" ,"apart" ,"appear" ,"appreciate"
            ,"appropriate" ,"are" ,"aren't" ,"around" ,"as" ,"a's" ,"aside" ,"ask" ,"asking"
            ,"associated" ,"at" ,"available" ,"away" ,"awfully",
                              "back" ,"backward" ,"backwards" ,"be" ,"became" ,"because" ,"become" ,"becomes"
            ,"becoming" ,"been" ,"before" ,"beforehand" ,"begin" ,"behind" ,"being" ,"believe"
            ,"below" ,"beside" ,"besides" ,"best" ,"better" ,"between" ,"beyond" ,"both" ,"brief"
            ,"but" ,"by" ,"came" ,"can" ,"cannot" ,"cant",
                              "can't" ,"caption" ,"cause" ,"causes" ,"certain" ,"certainly" ,"changes" ,"clearly"
            ,"c'mon" ,"co" ,"co." ,"com" ,"come" ,"comes" ,"concerning" ,"consequently" ,"consider"
            ,"considering" ,"contain" ,"containing" ,"contains" ,"corresponding" ,"could" ,"couldn't"
            ,"course" ,"c's" ,"currently",
                              "dare" ,"daren't" ,"definitely" ,"described" ,"despite" ,"did" ,"didn't" ,"different"
            ,"directly" ,"do" ,"does" ,"doesn't" ,"doing" ,"done" ,"don't" ,"down" ,"downwards"
            ,"during" ,"each" ,"edu" ,"eg" ,"eight" ,"eighty" ,"either" ,"else" ,"elsewhere" ,"end"
            ,"ending" ,"enough" ,"entirely",
                              "especially" ,"et" ,"etc" ,"even" ,"ever" ,"evermore" ,"every" ,"everybody" ,"everyone"
            ,"everything" ,"everywhere" ,"ex" ,"exactly" ,"example" ,"except" ,"fairly" ,"far"
            ,"farther" ,"few",
                              "fewer" ,"fifth" ,"first" ,"five" ,"followed" ,"following" ,"follows" ,"for" ,"forever"
            ,"former" ,"formerly" ,"forth" ,"forward" ,"found" ,"four" ,"from" ,"further"
            ,"furthermore" ,"get" ,"gets" ,"getting" ,"given" ,"gives" ,"go" ,"goes" ,"going" ,"gone"
            ,"got" ,"gotten" ,"greetings",
                              "had" ,"hadn't" ,"half" ,"happens" ,"hardly" ,"has" ,"hasn't" ,"have" ,"haven't"
            ,"having" ,"he" ,"he'd" ,"he'll" ,"hello" ,"help" ,"hence" ,"her" ,"here" ,"hereafter"
            ,"hereby" ,"herein" ,"here's" ,"hereupon" ,"hers" ,"herself" ,"he's" ,"hi" ,"him"
            ,"himself" ,"his" ,"hither" ,"hopefully" ,"how",
                              "howbeit" ,"however" ,"hundred" ,"i'd" ,"ie" ,"if" ,"ignored" ,"i'll" ,"i'm" ,"immediate"
            ,"in" ,"inasmuch" ,"inc" ,"inc." ,"indeed" ,"indicate" ,"indicated" ,"indicates" ,"inner"
            ,"inside" ,"insofar" ,"instead" ,"into" ,"inward" ,"is" ,"isn't" ,"it" ,"it'd" ,"it'll"
            ,"its" ,"it's" ,"itself",
                              "i've" ,"just" ,"k" ,"keep" ,"keeps" ,"kept" ,"know" ,"known" ,"knows" ,"last" ,"lately"
            ,"later" ,"latter" ,"latterly" ,"least" ,"less" ,"lest" ,"let" ,"let's" ,"like" ,"liked"
            ,"likely" ,"likewise" ,"little" ,"look" ,"looking" ,"looks" ,"low" ,"lower" ,"ltd" ,"made"
            ,"mainly" ,"make" ,"makes",
                              "many" ,"may" ,"maybe" ,"mayn't" ,"me" ,"mean" ,"meantime" ,"meanwhile" ,"merely"
            ,"might" ,"mightn't" ,"mine" ,"minus" ,"miss" ,"more" ,"moreover" ,"most" ,"mostly" ,"mr"
            ,"mrs" ,"much" ,"must" ,"mustn't" ,"my" ,"myself" ,"name" ,"namely" ,"nd" ,"near"
            ,"nearly" ,"necessary" ,"need" ,"needn't",
                              "needs" ,"neither" ,"never" ,"neverf" ,"neverless" ,"nevertheless" ,"new" ,"next" ,"nine"
            ,"ninety" ,"no" ,"nobody" ,"non" ,"none" ,"nonetheless" ,"noone" ,"no-one" ,"nor"
            ,"normally" ,"not" ,"nothing",
                              "notwithstanding" ,"novel" ,"now" ,"nowhere" ,"obviously" ,"of" ,"off" ,"often" ,"oh"
            ,"ok" ,"okay" ,"old" ,"on" ,"once" ,"one" ,"ones" ,"one's" ,"only" ,"onto" ,"opposite"
            ,"or" ,"other" ,"others" ,"otherwise" ,"ought" ,"oughtn't" ,"our" ,"ours" ,"ourselves"
            ,"out" ,"outside" ,"over",
                              "overall" ,"own" ,"particular" ,"particularly" ,"past" ,"per" ,"perhaps" ,"placed"
            ,"please" ,"plus" ,"possible" ,"presumably" ,"probably" ,"provided" ,"provides" ,"que"
            ,"quite" ,"qv" ,"rather" ,"rd" ,"re" ,"really" ,"reasonably" ,"recent" ,"recently"
            ,"regarding" ,"regardless" ,"regards",
                              "relatively" ,"respectively" ,"right" ,"round" ,"said" ,"same" ,"saw" ,"say" ,"saying"
            ,"says" ,"second" ,"secondly" ,"see" ,"seeing" ,"seem" ,"seemed" ,"seeming" ,"seems"
            ,"seen" ,"self" ,"selves" ,"sensible" ,"sent" ,"serious" ,"seriously" ,"seven" ,"several"
            ,"shall" ,"shan't" ,"she" ,"she'd",
                              "she'll" ,"she's" ,"should" ,"shouldn't" ,"since" ,"six" ,"so" ,"some" ,"somebody"
            ,"someday" ,"somehow" ,"someone" ,"something" ,"sometime" ,"sometimes" ,"somewhat"
            ,"somewhere" ,"soon" ,"sorry" ,"specified" ,"specify" ,"specifying" ,"still" ,"sub"
            ,"such" ,"sup" ,"sure" ,"take" ,"taken",
                              "taking" ,"tell" ,"tends" ,"th" ,"than" ,"thank" ,"thanks" ,"thanx" ,"that" ,"that'll"
            ,"thats" ,"that's" ,"that've" ,"the" ,"their" ,"theirs" ,"them" ,"themselves" ,"then"
            ,"thence" ,"there" ,"thereafter",
                              "thereby" ,"there'd" ,"therefore" ,"therein" ,"there'll" ,"there're" ,"theres" ,"there's"
            ,"thereupon" ,"there've" ,"these" ,"they" ,"they'd" ,"they'll" ,"they're" ,"they've"
            ,"thing" ,"things" ,"think" ,"third" ,"thirty" ,"this" ,"thorough" ,"thoroughly" ,"those"
            ,"though" ,"three",
                              "through" ,"throughout" ,"thru" ,"thus" ,"till" ,"to" ,"together" ,"too" ,"took"
            ,"toward" ,"towards" ,"tried" ,"tries" ,"truly" ,"try" ,"trying" ,"t's" ,"twice" ,"two"
            ,"un" ,"under" ,"underneath" ,"undoing" ,"unfortunately" ,"unless" ,"unlike" ,"unlikely"
            ,"until" ,"unto" ,"up" ,"upon",
                              "upwards" ,"us" ,"use" ,"used" ,"useful" ,"uses" ,"using" ,"usually" ,"v" ,"value"
            ,"various" ,"versus" ,"very" ,"via" ,"viz" ,"vs" ,"want" ,"wants" ,"was" ,"wasn't" ,"way"
            ,"we" ,"we'd" ,"welcome" ,"well" ,"we'll" ,"went" ,"were" ,"we're" ,"weren't" ,"we've"
            ,"what" ,"whatever" ,"what'll",
                              "what's" ,"what've" ,"when" ,"whence" ,"whenever" ,"where" ,"whereafter" ,"whereas"
            ,"whereby" ,"wherein" ,"where's" ,"whereupon" ,"wherever" ,"whether" ,"which" ,"whichever"
            ,"while" ,"whilst" ,"whither" ,"who" ,"who'd" ,"whoever" ,"whole" ,"who'll" ,"whom"
            ,"whomever" ,"who's" ,"whose",
                              "why" ,"will" ,"willing" ,"wish" ,"with" ,"within" ,"without" ,"wonder" ,"won't" ,"would"
            ,"wouldn't" ,"yes" ,"yet" ,"you" ,"you'd" ,"you'll" ,"your" ,"you're" ,"yours" ,"yourself"
            ,"yourselves" ,"you've" ,"zero" ,"a" ,"how's" ,"i" ,"when's" ,"why's" ,"b" ,"c" ,"d" ,"e"
            ,"f" ,"g" ,"h" ,"j" ,"l" ,"m",
                              "n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"uucp" ,"w" ,"x" ,"y" ,"z" ,"I" ,"www" ,"amount"
            ,"bill" ,"bottom" ,"call" ,"computer" ,"con" ,"couldnt" ,"cry" ,"de" ,"describe" ,"detail"
            ,"due" ,"eleven" ,"empty" ,"fifteen",
                              "fifty" ,"fill" ,"find" ,"fire" ,"forty" ,"front" ,"full" ,"give" ,"hasnt" ,"herse"
            ,"himse" ,"interest" ,"itse”" ,"mill" ,"move" ,"myse”" ,"part" ,"put" ,"show" ,"side"
            ,"sincere" ,"sixty" ,"system" ,"ten" ,"thick" ,"thin" ,"top" ,"twelve" ,"twenty" ,"abst"
            ,"accordance" ,"act" ,"added",
                              "adopted" ,"affected" ,"affecting" ,"affects" ,"ah" ,"announce" ,"anymore" ,"apparently"
            ,"approximately" ,"aren" ,"arent" ,"arise" ,"auth" ,"beginning" ,"beginnings" ,"begins"
            ,"biol" ,"briefly" ,"ca" ,"date" ,"ed" ,"effect" ,"et-al" ,"ff" ,"fix" ,"gave" ,"giving"
            ,"heres" ,"hes" ,"hid",
                              "home" ,"id" ,"im" ,"immediately" ,"importance" ,"important" ,"index" ,"information"
            ,"invention" ,"itd" ,"keys" ,"kg" ,"km" ,"largely" ,"lets" ,"line" ,"'ll" ,"means" ,"mg"
            ,"million" ,"ml" ,"mug" ,"na" ,"nay" ,"necessarily" ,"nos" ,"noted" ,"obtain" ,"obtained"
            ,"omitted" ,"ord" ,"owing",
                              "page" ,"pages" ,"poorly" ,"possibly" ,"potentially" ,"pp" ,"predominantly" ,"present"
            ,"previously" ,"primarily" ,"promptly" ,"proud" ,"quickly" ,"ran" ,"readily" ,"ref"
            ,"refs" ,"related" ,"research" ,"resulted" ,"resulting" ,"results" ,"run" ,"sec"
            ,"section" ,"shed" ,"shes" ,"showed",
                              "shown" ,"showns" ,"shows" ,"significant" ,"significantly" ,"similar" ,"similarly"
            ,"slightly" ,"somethan" ,"specifically" ,"state" ,"states" ,"stop" ,"strongly"
            ,"substantially" ,"successfully" ,"sufficiently",
                              "suggest" ,"thered" ,"thereof" ,"therere" ,"thereto" ,"theyd" ,"theyre" ,"thou"
            ,"thoughh" ,"thousand" ,"throug" ,"til" ,"tip" ,"ts" ,"ups" ,"usefully" ,"usefulness"
            ,"'ve" ,"vol" ,"vols" ,"wed" ,"whats" ,"wheres" ,"whim" ,"whod" ,"whos" ,"widely" ,"words"
            ,"world" ,"youd" ,"youre" ,"'", "'", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def isStopWord(self, word):
        return word in self._stopWordList

    def removeStopWords(self, paragraph :str) -> str:
        if len(paragraph) == 0:
            return ""
        wordsList : list = paragraph.split(' ')
        wordsListIndex = 0
        newParagraph = ""

        while wordsListIndex < len(wordsList):
            currentWord = self.removePunctuations(wordsList[wordsListIndex])
            if not self.isStopWord(currentWord):
                newParagraph = newParagraph + " " + currentWord
            wordsListIndex = wordsListIndex + 1
        return newParagraph

    def removePunctuations(self, word: str):
        if len(word) == 0:
            return ""
        ## lower case the word
        word = word.lower()
        puntuationList = [",",":",".", "?", ";", ":", "/", "(", ")", "-","!", "`", "’"]
        charIndex = 0
        newWord = ""
        while charIndex < len(word):
            if word[charIndex] not in puntuationList:
                newWord = newWord + word[charIndex]
            charIndex = charIndex + 1
        return newWord