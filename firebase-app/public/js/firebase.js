// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.3.1/firebase-app.js";
import { GoogleAuthProvider, getRedirectResult, getAuth, signInWithRedirect, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.3.1/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBuygMmEKiSF_pvzbRZrl0EGWM5HhB6AXU",
  authDomain: "ec463miniproject-c8a9f.firebaseapp.com",
  projectId: "ec463miniproject-c8a9f",
  storageBucket: "ec463miniproject-c8a9f.appspot.com",
  messagingSenderId: "883850515705",
  appId: "1:883850515705:web:56c226eee2bc2aa2e57e28"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();
const provider = new GoogleAuthProvider();

let currentUser = null;
onAuthStateChanged(auth, user => currentUser = user);

const redirectResult = await getRedirectResult(auth).catch(() => null);

if (!redirectResult && !currentUser) { signInWithRedirect(auth, provider); }

// getRedirectResult(auth)
//   .then((result) => {
//     // This gives you a Google Access Token. You can use it to access Google APIs.
//     const credential = GoogleAuthProvider.credentialFromResult(result);
//     const token = credential.accessToken;

//     // The signed-in user info.
//     const user = result.user;
//     // IdP data available using getAdditionalUserInfo(result)
//     // ...
//   }).catch((error) => {
//     // Handle Errors here.
//     const errorCode = error.code;
//     const errorMessage = error.message;
//     // The email of the user's account used.
//     const email = error.customData.email;
//     // The AuthCredential type that was used.
//     const credential = GoogleAuthProvider.credentialFromError(error);
//     // ...
//   });


// signInWithRedirect(auth, provider);
debugger;
// onAuthStateChanged(auth, user => {
//   if (user) {
//     // User is signed in.
//     console.log('user is logged in');
//   } else {
//     console.log('user is not logged in')
//   }
// })
