import { writable } from 'svelte/store';

function getSavedToken() {
  if (typeof window !== 'undefined') {
    return localStorage.getItem('auth_token');
  }
  return null;
}

export const authToken = writable(getSavedToken());
