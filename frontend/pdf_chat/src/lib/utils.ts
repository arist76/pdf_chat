export const getCookieValue = (cookieName : string) => {
    const name = cookieName + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');

    for(let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i].trim();
        if (cookie.indexOf(name) === 0) {
        return cookie.substring(name.length, cookie.length);
        }
    }
    return null; // Return null if the cookie with the given name is not found
}
