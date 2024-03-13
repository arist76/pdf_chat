import { token } from '$lib/store';
import { redirect } from '@sveltejs/kit';
/** @type {import('@sveltejs/kit').Handle} */

// define the routes of we want to be possible to access without auth
const public_paths = ['/signup', '/signin'];

// function to verify if the request path is inside the public_paths array
function isPathAllowed(path: string) {
	return public_paths.some(
		(allowedPath) => path === allowedPath || path.startsWith(allowedPath + '/')
	);
}

export const handle = async ({ event, resolve }) => {
	let tokenVal: string | null | undefined = null;

	// check if the cookie exist, and if exists, parse it to the user variable
	if (event.cookies.get('auth_token') != undefined && event.cookies.get('auth_token') != null) {
		tokenVal = event.cookies.get('auth_token');
	}
	const url = new URL(event.request.url);

	// validate the user existence and if the path is acceesible
	if (!tokenVal && !isPathAllowed(url.pathname)) {
		throw redirect(302, '/signin');
	}

	if (tokenVal) {
		// redirect user if he is already logged if he try to access signin or signup
		if (url.pathname == '/signup' || url.pathname == '/signin') {
			throw redirect(302, '/');
		}
		token.set(tokenVal);
		
	}

	const response = await resolve(event);

	return response;
};
