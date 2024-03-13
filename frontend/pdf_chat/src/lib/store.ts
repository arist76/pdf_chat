import { writable, type Writable } from 'svelte/store';
import { getCookieValue } from './utils';

export const token: Writable<null | string> = writable(null);

// On client side, update token with the value from cookie
if (typeof window !== 'undefined') {
	const initialToken = getCookieValue('auth_token');
	if (initialToken) {
		token.set(initialToken);
	}
}

