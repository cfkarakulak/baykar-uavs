<script>
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';
	import token from '../../stores/auth';

	if (browser && $token) {
		goto('/uav');
	}

	const credentials = {
		username: '',
		password: ''
	};

	async function login() {
		await loginLocal(credentials);
	}

	let error = '';

	async function loginLocal(credentials) {
		const res = await fetch('http://localhost:8000/api/v1/auth/token/', {
			method: 'POST',
			body: JSON.stringify(credentials),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		const data = await res.json();

		if (data.access) {
			token.set(data.access);
			goto('/uav');
		} else {
			error = 'Incorrect username or password';
			console.log(data);
		}
	}
</script>

<svelte:head>
	<title>Authenticate</title>
</svelte:head>

{#if !$token}
	<form>
		<h1 class="h3 mb-3 fw-normal text-center">Please sign in</h1>

		<div class="w-full max-w-xs mx-auto">
			<form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
				<div class="mb-4">
					<label class="block text-gray-700 text-sm font-bold mb-2" for="username">
						Username
					</label>
					<input
						bind:value={credentials.username}
						class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
						id="username"
						type="text"
						placeholder="Username"
					/>
				</div>

				<div class="mb-6">
					<label class="block text-gray-700 text-sm font-bold mb-2" for="password">
						Password
					</label>
					<input
						bind:value={credentials.password}
						class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
						id="password"
						type="password"
						placeholder="******************"
					/>
				</div>

				<div class="flex items-center justify-between">
					<button
						class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
						on:click|preventDefault={login}
					>
						Sign In
					</button>
				</div>
			</form>

			<p class="text-center text-red-500 mt-4 text-xs">{error}</p>
		</div>
	</form>
{/if}
