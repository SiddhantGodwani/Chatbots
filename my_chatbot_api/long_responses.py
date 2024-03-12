import random
#add your bots answers here and use the name of the leyword as long.name in place of the 'answer statement'

R_EATING = "I don't like eating oviously! ,cus I'm a Bot"

#answers of the questions--------------------------------------------------------

a0="E-waste is old electronic devices that we throw away."

a1= "E-waste is old electronic devices that we throw away. It's a concern because it can harm the environment and our health."

a2  = "To dispose of old electronics responsibly, recycle them at special centers or programs. Make sure to remove your data first."

a3  = "You can recycle old cell phones and tablets at local recycling centers or through manufacturer programs."

a4  = "Regulations on e-waste disposal vary by location. Check with your local government for the rules in your area."

a5  = "Improper e-waste disposal can pollute soil, water, and air, and release harmful substances into the environment."

a6  = "Reduce, reuse, and recycle means use your electronics longer, repair them, or recycle them when you're done."

a7  = "Recycle chargers and cables at e-waste centers, and don't throw them in the trash."

a8  = "Many organizations and governments hold e-waste collection events. Check online or with your local authorities for details."

a9  = "Common recyclable parts include metals, plastics, circuit boards, and batteries. Precious metals like gold can also be recovered."

a10  = " To protect your data, use data wiping software or professional data destruction services before recycling old electronics."

a11  = " Improper e-waste disposal can expose people to toxic chemicals and heavy metals, causing health issues."

a12  = " Recycling e-waste conserves resources, reduces mining, and can create jobs, helping the economy."

a13  = " Businesses can set up e-waste recycling programs, work with certified recyclers, and educate employees for responsible disposal."

a14  = " Various initiatives and innovations aim to improve e-waste recycling methods."

a15  = " To extend electronic device lifespan, consider repairs, upgrades, or donating them instead of disposal."

a16  = "you can easily find the nearest ewaste recycling center by using our website location based search,just enter your address, and we'll provide you with a list of nearby recycling centers."
a17  = "you can recycle your old electronics at any of the ewaste recycling centers listed on our website. "
a18  = "our website allows you to find ewaste recycling centers specifically in your chosen city or area. simply input the location, and we'll provide you with a list of relevant centers."
a19  = "our website provides comprehensive information about ewaste recycling programs tailored to your city or area."
a20  = "our credit system rewards users for responsibly recycling electronic waste through our ewaste facility locator. when you recycle, you earn credits that can be redeemed for various benefits."
a21  = "earning credits through our ewaste facility locator offers several benefits. you can redeem them for discounts, participate in special promotions, and even support environmental causes."
a22  = "certainly, when you recycle electronic waste through our system, you earn credits based on the type and quantity of items recycled. the more you recycle, the more credits you accumulate."
a23  = "fistly click on to the buy option mentioned on to the homepage. select your material you want to buy. click on to buy the material. go through all the further procedure."
a24  = "while we have some guidelines, generally, users can sell a wide range of items on our platform. however, certain prohibited items are not allowed."
a25  = " yes, we have a rating system where buyers and sellers can leave feedback and ratings based on their transactions. it helps build trust within our community."
a26  = " to list an item for sale on our platform, follow these steps: create an account, provide item details, set a price, and upload images. Your item will be visible to potential buyers."
a27  = " we provide the service of nearest ewaste locations nearby your area, also provides you to buy and sell the products and can earn credit points. our moto is to utilize the ewaste products and make them use."
a28  = " i'm just a chatbot, so i don't have a name. You can call me etrashify."
a29  = " i'm here to provide information on ewaste facilities ."
a30  = " i can provide news and updates on various subjects. if you have a specific topic in mind, feel free to ask."
a31  = " i'm a virtual assistant designed to provide information and assist with tasks. i'm constantly learning to better help users like you."
a32  = " your interaction and questions make my day. just feel free to engage with me, and I'll do my best to assist you."
a33  = " i'm here to help you make the most of our website. feel free to ask questions or seek assistance with any task."
a34  = " certainly, i can guide you through the account creation process step by step:/n>> click on the login page/n >>enter your username/n >>enter your password/n >>password should contain lowercase only/n >>click on submit button"
a35  = " i can help you find specific content or guide you through our website's categories."
a36  = " click on find location , if the location appears visit to the location. If the location does not appear then may be no nearby loactions near or some glitch."


















#add negative/unknown responses here💀
def unknown():
    response = ['could you please re-phrase that',
                '....',
                "i don't know",
                "sorry.....?",
                "sound about right",
                "what do you mean",
                "I am sorry can you please make sure you are using the right kewords",
                "Can you check if you are spelling it correctly"][random.randrange(8)]
    return response