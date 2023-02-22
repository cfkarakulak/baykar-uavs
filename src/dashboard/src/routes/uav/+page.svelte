<script lang="ts">
	import { onMount } from 'svelte';
	import Table from '../../components/Table.svelte';
	import token from '../../stores/auth';
	import { browser } from '$app/environment';
	import { goto } from '$app/navigation';

	if (browser && !$token) {
		goto('/login');
	}

	type Uav = {
		createdAt: Date;
		image: any;
		content: string;
		title: string;
		id: number;
	};

	let items: Uav[] = [];
	let loaded = false;

	onMount(() => loadData());

	function logout() {
		$token = null;

		if (browser) {
			window.localStorage.removeItem('token');
		}

		goto('/login');
	}

	async function loadData() {
		loaded = false;

		const res = await fetch('http://localhost:8000/api/v1/uavs/', {
			method: 'GET',
			headers: {
				Authorization: `Bearer ${$token}`,
				'Content-Type': 'application/json'
			}
		});

		const data = await res.json();

		if (res.status == 401) {
			logout();
		}

		items = data.results;
		loaded = true;
	}
</script>

<svelte:head>
	<title>List of UAVs</title>
</svelte:head>

{#if $token}
	<div class="mb-8">
		<div class="w-64 mx-auto">
			<h1 class="h3 mb-3 fw-normal text-center">
				You can view, create/update and delete your UAVs
			</h1>
			<a
				href="/uav/new"
				class="inline-block w-full mx-auto text-center bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
				>Create a new one</a
			>
		</div>
	</div>

	<div class="w-3/4 mx-auto">
		<Table {items} {loaded} />
	</div>

	<button on:click={logout} class="table mt-8 w-64 mx-auto text-center mx-auto text-gray-500 mt-4"
		>Log out
	</button>
{/if}
