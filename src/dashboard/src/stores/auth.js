import { browser } from '$app/environment';
import { writable } from 'svelte/store';

const initialValue = browser ? window.localStorage.getItem('token') : null;

const token = writable(initialValue);

token.subscribe((value) => {
    if (browser && value) {
        window.localStorage.setItem('token', value);
    }
});
  
export default token;
