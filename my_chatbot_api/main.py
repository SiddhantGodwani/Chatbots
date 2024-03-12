import re #for rejects
import long_responses as long   


print("Hello! I am you ChatBot LOKI\nHow can I assist you today?")
#rec_words = array of words we want the bot to recognise
def message_probability(user_message,recognised_words,single_response=False,required_words=[]):
    message_certainty=0
    has_required_words=True
    
#recognising text
    for word in user_message:
        if word in required_words:
            message_certainty+=1           #more accurate
            
    #calculate the (accuracy)percentage of required wordds in user msg
    percentage = float (message_certainty) / float(len(recognised_words))

    #now check if required words are included or not
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    #creating return statement that returns the accuracy of each statement to be compared for best response possible
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0          #means nothing matched returning lowest value possible    


def check_all_messages(message):
    highest_prob_list = {}
    #helper fxn
    def response(bot_response,list_of_words,single_response = False,required_words = {}):
        nonlocal highest_prob_list  #global 
        #simplifies adding items to our dictionary
        highest_prob_list[bot_response]=message_probability(message,list_of_words,single_response,required_words)
        #easier way to insert key &------------------------->value
        
        
        
        
        
    
#RESPONSES-------------------------------------------------------------------------
# yaha bot ke rsponses dalne hai 
#format   response,[keywords required for getting that response], required word 

    #response('Hello!',['hello','hi','sup','hey','yo','aur'], single_response = True)
    response('Hello!,How may I help you',['hi'],  required_words=['hi'])
    response('Hello!!,How may I help you',['hey'], required_words=['hey'])
    response('Hello!!,How may I help you',['sup'], required_words=['sup'])
    response('Hello!!,How may I help you',['hi'], required_words=['hi'])
    response('Hello!!,How may I help you',['yo'], required_words=['yo'])
    response('Hello!!,How may I help you',['aur'], required_words=['aur'])
    response('I\'m doing,fine, and you',['how','are','you','doing'],required_words=['how'])
    response(long.R_EATING, ['what','you','eat'], required_words=['you','eat'])
    #response("I don't like eating oviously! ,cus I'm a Bot", ['what','you','eat'],required_words=['eat'])
    response(long.a1,['what', 'is', 'e','waste,', 'and', 'why', 'is', 'it', 'a', 'concern'],required_words=['e','waste','concern'] )
    response(long.a0,['what', 'is', 'e','waste,'],required_words=['e','waste'] )
    response(long.a2, ['how', 'should', 'I', 'dispose', 'of', 'old', 'electronic', 'devices', 'responsibly'],required_words=[ 'dispose', 'electronic', 'devices',])
    response(long.a3, ['where', 'can', 'I', 'recycle', 'old', 'cell', 'phones', 'and', 'tablets'],required_words=[ 'recycle', 'old', 'cell', 'phones'] )
    response(long.a4, ['are', 'there', 'any', 'regulations', 'regarding', 'e','waste', 'disposal', 'in', 'my', 'area'],required_words=[ 'regulations'])
    response(long.a5, ['what', 'are', 'the', 'environmental', 'impacts', 'of', 'improper', 'e','waste', 'disposal'],required_words=[ 'environmental', 'impacts', 'improper'])
    response(long.a6, ['can', 'you', 'explain', 'the', 'concept', 'of', '"reduce,', 'reuse,', 'and', 'recycle"', 'in', 'the', 'context', 'of', 'e-waste'],required_words=[ 'reduce,','reuse,', 'recycle'])
    response(long.a7, ['what', 'should', 'I', 'do', 'with', 'electronic', 'accessories', 'like', 'chargers', 'and', 'cables', 'when', "they're", 'no', 'longer', 'needed'],required_words=[ 'do', 'electronic', 'accessories', 'needed'])
    response(long.a8, ['are', 'there', 'any', 'organizations', 'or', 'programs', 'that', 'offer', 'e','waste', 'collection', 'events', 'or', 'drop-off', 'locations'],required_words=[ 'organizations', 'offer', 'e','waste', 'collection'])
    response(long.a9, ['what', 'are', 'some', 'common', 'components', 'of', 'electronic', 'devices', 'that', 'can', 'be', 'recycled'],required_words=[ 'common', 'components','recycled'])
    response(long.a10, ['how', 'can', 'I', 'ensure', 'that', 'my', 'personal', 'data', 'is', 'securely', 'removed', 'from', 'old', 'electronics', 'before', 'recycling', 'them'],required_words=[ 'ensure', 'personal', 'data', 'securely',])
    response(long.a11,  ['tell', 'me', 'about', 'the', 'potential', 'health', 'hazards', 'associated', 'with', 'improper', 'e','waste', 'disposal.'],required_words=[ 'improper', 'e','waste', 'disposal'])
    response(long.a12, ['what', 'are', 'the', 'economic', 'benefits', 'of', 'recycling', 'e','waste'],required_words=[ 'economic', 'benefits', 'recycling', 'e','waste'])
    response(long.a13, ['how', 'can', 'businesses', 'responsibly', 'manage', 'e','waste', 'generated', 'by', 'their', 'operations'],required_words=[ 'businesses', 'manage', 'e','waste', 'generated',])
    response(long.a14,['are', 'there', 'any', 'initiatives', 'or', 'innovations', 'in', 'e','waste', 'recycling', 'that', 'I', 'should', 'be', 'aware', 'of'],required_words=[ 'initiatives', 'innovations', 'e','waste', 'recycling', 'aware'])
    response(long.a15, ['what', 'are', 'some', 'alternatives', 'to', 'disposal', 'for', 'extending', 'the', 'lifespan', 'of', 'electronic', 'devices'],required_words=[ 'extending', 'lifespan', 'electronic', 'devices'])
    response(long.a16,['find','the','nearest','ewaste','recycling','center'],required_words=['find','ewaste','center'])
    response(long.a17,['where','can','i','recycle','my','old','electronics'],required_words=['where','recycle'])
    response(long.a18,['find','ewaste','recycling','centers','in','area'],required_words=['find','centers'])
    response(long.a19,['tell','me','about','ewaste','recycling','programs','in','area'],required_words=['tell','recycling','programs'])
    response(long.a20,['how','does','the','credit','system','work','for','using','the','ewaste','facility','locator'],required_words=['credit','facility','locator'])
    response(long.a21,['what','are','the','benefits','of','earning','credits','through','the','ewaste','facility','locator'],required_words=['benefits','credits'])
    response(long.a22,['can','you','explain','the','process','of','earning','credits','by','recycling','electronic','waste'],required_words=['process','earning'])
    response(long.a23,['how','does','the','buying','process','work','on','your','website'],required_words=['buying','website'])
    response(long.a24,['are','there','any','restrictions','on','the','types','of','items','that','can','be','sold','or','brought','on','your','platform'],required_words=['types','sold','platform'])
    response(long.a25,['is','there','a','rating','system','for','sellers','and','buyers','on','your','system'],required_words=['rating','buyers'])
    response(long.a26,['what','are','the','steps','to','list','an','item','for','sale','on','your','platform'],required_words=['list','item','sale'])
    response(long.a27,['what','are','the','services','of','our','website'],required_words=['services','what'])
    response(long.a28,['whats','your','name'],required_words=['name'])
    response(long.a29,['do','you','have','any','preferences','for','the','type','of','information','your','looking','for'],required_words=['preferences','information','looking'])
    response(long.a30,['are','you','interested','in','recent','news','or','updates','on','any','particular','subject'],required_words=['news','updates','subject'])
    response(long.a31,['tell','me','a','bit','about','yourself'],required_words=['bit','about','yourself'])
    response(long.a32,['what','can', 'i','do','to','make','your','day','better'],required_words=['do','make','day'])
    response(long.a33,['how','can','i','assist','you','with','using','our','website','today'],required_words=['can','with'])
    response(long.a34,['can','i','help','you','create','an','account','and','set','up','your','profile','on','our','website'],required_words=['an','and','on'])
    response(long.a35,['how','can','i','assist','you','in','navigating','through','our','website','content'],required_words=['assist','website'])
    response(long.a36,['there','is','not','any','nearby','ewaste','locations','to','be','found'],required_words=['is','not','any'])

    
    
    
    
    
    
    
    
    
    
    
    best_match = max(highest_prob_list, key = highest_prob_list.get)
    #print(highest_prob_list)
    
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match
    #return best_match
    




#===========================================================================================
#ye fxn user input leta hai
def get_response(user_input):
#splits the message into an array so that we can analyze each word seperately from the user message 
    split_message= re.split(r'\s+|[,;!.-]\s*', user_input.lower())  #re removes symbols frm messages and lower lowercases the msg
    response = check_all_messages(split_message)
    return response



#infinite while ttrue loop hai ye fr new responses
#Response system 
while True:
    print('Bot: '+ get_response(input('You: ')))
