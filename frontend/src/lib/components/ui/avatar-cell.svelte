<script lang="ts">
	import * as Avatar from '$lib/components/ui/avatar';

	export let name: string;
</script>

<Avatar.Root class="h-6 w-6 transition-all hover:scale-125">
	<Avatar.Image
		src={`https://api.dicebear.com/9.x/personas/svg?seed=${name}&backgroundColor=c4e2f2`}
		alt={name}
		class=""
	/>
	<Avatar.Fallback>{name.toUpperCase().charAt(0)}</Avatar.Fallback>
</Avatar.Root>
