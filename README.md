# HackCMU 2023 - Space Face
*by Melody Hu, Irene Pi, and Angela Lou*

If you are a parent, you probably don't want your kids to check out and buy stuff on Amazon without your consent. But, you still want them to choose what they would like on Amazon. This is a Chrome browser extension that doesn't let anyone proceed to the checkout page until a known face (ideally, parent's face) is recognized via the web camera. Also, because HackCMU's theme this year is space, we added space helmets on everyone's faces identified on the web camera when scanning for known people :) Here are each of the components of the project in detail:

## Facial Recognition (cv)
- **technologies**: Python, OpenCV, face_recognition library
- **features**: facial recognition, open webcam for set period of time, space helmet filter
- **steps**:
  1. open webcam
  2. load known faces
  3. for 15 secs, use face_recognition to identify faces in webcam and compare to known
  4. apply space helmet to everyone on webcam :)
  5. once it matches someone to known face, print out "accept"
- **resources**:
  - facial recognition: [https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam.py](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam.py)
  - filter on faces: [https://github.com/TithiSreemany/Snapchat-Filter-using-OpenCV/blob/main/Snapchat%20Filter%20with%20OpenCV.ipynb](https://github.com/TithiSreemany/Snapchat-Filter-using-OpenCV/blob/main/Snapchat%20Filter%20with%20OpenCV.ipynb)
  - space helmet: [image link](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vecteezy.com%2Fpng%2F1205932-astronaut-helmet&psig=AOvVaw2F2hOIEZSc3UDFCzbROogi&ust=1694963955772000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCIiG3_W2r4EDFQAAAAAdAAAAABAQ)

## Chrome extension (chrome extension)
- **technologies**: HTML, CSS, JavaScript
- **features**: buttons accept(green) -> successfully continue to purchase, reject(red) -> invader link, upload known image(user to upload image for facial recognition)
  **Other features**: highlight a word + right click + search word on Amazon
- **steps**:
  1. open Google Chrome (works better on non-dark mode) & manage Extensions
  2. toggle on Developer Mode & click on "Load Unpacked"
  3. upload the "chrome-extension" folder
  4. once uploaded, go to the Extension icon at the top of the browser
  5. click on "View popup"
- **resources**:
  - chrome extension: [SteamCode Chrome Extension](https://www.youtube.com/channel/UClLRjv91UloHweZMyxpRPrw) 

## Mock website (website)
- **technologies**: HTML, CSS, JavaScript
- **features**: picture slideshow, button that launches chrome extension
- **steps**:
  1. slideshow shows pictures of space and mars to advertise the tour tickets
  2. user will click buy tickets, which launches the chrome extension 
  3. after their face is verified, user can continue with the purchase
- **resources**:
  - obrion-nebula: [image link](https://pixabay.com/photos/orion-nebula-emission-nebula-11107/)
